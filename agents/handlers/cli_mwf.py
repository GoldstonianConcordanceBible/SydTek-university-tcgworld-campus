from __future__ import annotations
import json
import sys
from pathlib import Path

from config.load_config import load_config
from routing.router import route_text
from runtime.dispatch import dispatch

def main() -> int:
    cfg = load_config("config/config.yml")

    text = ""
    if not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:]).strip()

    if not text:
        print("Usage: echo 'text' | python cli_mwf.py\n   or: python cli_mwf.py 'text to route'")
        return 2

    decision = route_text(
        text=text,
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=cfg.policy_enabled,
        embed_enabled=cfg.embed_enabled,
        embed_model_name=cfg.embed_model_name,
        embed_threshold=cfg.embed_threshold,
        embed_top_k=cfg.embed_top_k,
        fuzzy_enabled=getattr(cfg, "fuzzy_enabled", True),
        fuzzy_threshold=getattr(cfg, "fuzzy_threshold", 90.0),
        context_radius_chars=getattr(cfg, "context_radius_chars", 120),
    )

    out = dispatch(text=text, decision=decision.to_dict(), state={})
    payload = {
        "decision": decision.to_dict(),
        "mirror": out.mirror,
        "water": out.water,
        "fire": out.fire,
        "metadata": out.metadata,
    }
    print(json.dumps(payload, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())