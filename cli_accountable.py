from __future__ import annotations
import json
import sys
from pathlib import Path

from config.load_config import load_config
from routing.router import route_text
from runtime.dispatch import dispatch
from runtime.apply_action import apply_policy_action

from accountability.hash import decision_hash
from accountability.approvals import new_approval
from accountability.ledger import append_record
from accountability.exporter import export_bundle

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
    payload = {
        "decision": decision.to_dict(),
        "mirror": handled.mirror,
        "water": handled.water,
        "fire": handled.fire,
        "metadata": handled.metadata,
    }

    # Apply allow/rewrite/block/escalate
    action_result = apply_policy_action(payload)
    final_payload = action_result.output

    # Hash the *decision contract* (stable)
    d_hash = decision_hash(final_payload["decision"])

    # Approvals (example: auto-approve allow; require review otherwise)
    approved = action_result.action == "allow"
    approver = "agent:router"
    reason = "auto-approved (allow)" if approved else f"auto-flagged ({action_result.action})"

    approval = new_approval(
        decision_hash=d_hash,
        approved=approved,
        approved_by=approver,
        approval_reason=reason,
        policy_version="route_policies:v1",
        router_version=final_payload["decision"].get("version", "unknown"),
    ).to_dict()

    # Ledger entry (full)
    ledger_entry = {
        "decision_hash": d_hash,
        "payload": final_payload,
        "approval": approval,
    }
    append_record(ledger_entry)

    # Export bundle (compact anchoring artifact)
    bundle = export_bundle(
        decision_hash_hex=d_hash,
        decision=final_payload["decision"],
        mirror=final_payload["mirror"],
        water=final_payload["water"],
        fire=final_payload["fire"],
        approval=approval,
        out_path="accountability/bundles/latest.bundle.json",
    )

    out = {
        "action": action_result.action,
        "decision_hash": d_hash,
        "bundle": bundle,
        "payload": final_payload,
    }
    print(json.dumps(out, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())