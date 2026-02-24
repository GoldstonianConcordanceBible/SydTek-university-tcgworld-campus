from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple

from config.load_config import load_config
from routing.router import route_text

CASES_DIR = Path("tests/fixtures/cases")
EXP_DIR = Path("tests/fixtures/expected")

def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))

def evaluate_case(case: Dict[str, Any], expected: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
    cfg = load_config("config/config.yml")

    overrides = case.get("config_overrides", {})
    decision = route_text(
        text=case["text"],
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=overrides.get("policy_enabled", cfg.policy_enabled),
        embed_enabled=overrides.get("embed_enabled", cfg.embed_enabled),
        embed_model_name=overrides.get("embed_model_name", cfg.embed_model_name),
        embed_threshold=overrides.get("embed_threshold", cfg.embed_threshold),
        embed_top_k=overrides.get("embed_top_k", cfg.embed_top_k),
        fuzzy_enabled=overrides.get("fuzzy_enabled", getattr(cfg, "fuzzy_enabled", True)),
        fuzzy_threshold=overrides.get("fuzzy_threshold", getattr(cfg, "fuzzy_threshold", 90.0)),
        context_radius_chars=overrides.get("context_radius_chars", getattr(cfg, "context_radius_chars", 120)),
    )

    ok = True
    exp_route = expected.get("expected_route")
    exp_any = expected.get("expected_route_any_of")
    min_hits = int(expected.get("min_policy_hits", 0))

    if exp_route is not None:
        ok = ok and (decision.route == exp_route)

    if exp_any is not None:
        ok = ok and (decision.route in exp_any)

    ok = ok and (len(decision.policy_hits) >= min_hits)

    report = {
        "id": case["id"],
        "text": case["text"],
        "decision": decision.to_dict(),
        "expected": expected,
        "pass": ok,
    }
    return ok, report

def main() -> int:
    case_files = sorted(CASES_DIR.glob("*.json"))
    results: List[Dict[str, Any]] = []
    passed = 0

    for cf in case_files:
        ef = EXP_DIR / (cf.stem + ".expected.json")
        if not ef.exists():
            raise FileNotFoundError(f"Missing expected file for {cf.name}: {ef}")

        case = load_json(cf)
        expected = load_json(ef)
        ok, report = evaluate_case(case, expected)
        results.append(report)
        passed += 1 if ok else 0

    total = len(results)
    score = (passed / total * 100.0) if total else 0.0

    out = {
        "total": total,
        "passed": passed,
        "failed": total - passed,
        "score_percent": round(score, 2),
        "results": results,
    }

    Path("tests/fixtures/report.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ["total", "passed", "failed", "score_percent"]}, indent=2))
    return 0 if passed == total else 1

if __name__ == "__main__":
    raise SystemExit(main())