from __future__ import annotations
import json
import sys
from pathlib import Path

from config.load_config import load_config
from routing.router import route_text
from runtime.dispatch import dispatch
from accountability.hash import decision_hash
from accountability.approvals import new_approval
from accountability.ledger import append_record

def main() -> int:
    cfg = load_config("config/config.yml")

    text = ""
    if not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:]).strip()

    if not text:
        print("Usage: echo 'text' | python cli_accountable.py")
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

    handled = dispatch(text=text, decision=decision.to_dict(), state={})

    d_hash = decision_hash(decision.to_dict())

    # Optional approval via env vars or later UI hook
    # For now: auto-approve non-policy routes as example
    approved = decision.route not in ("policy_review", "policy_review_strict")
    approver = "agent:router"
    reason = "auto-approved (non-policy route)" if approved else "needs review (policy route)"

    approval = new_approval(
        decision_hash=d_hash,
        approved=approved,
        approved_by=approver,
        approval_reason=reason,
        policy_version="phrase_lists:v1",
        router_version=decision.to_dict().get("version", "unknown"),
    )

    ledger_entry = {
        "decision_hash": d_hash,
        "decision": decision.to_dict(),
        "mirror": handled.mirror,
        "water": handled.water,
        "fire": handled.fire,
        "approval": approval.to_dict(),
    }
    append_record(ledger_entry)

    print(json.dumps(ledger_entry, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())