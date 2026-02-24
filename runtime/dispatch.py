from __future__ import annotations
from importlib import import_module
from typing import Dict, Any, Optional

from handlers.base import HandlerOutput
from policy.policy_engine import evaluate_policy

ROUTE_TO_HANDLER = {
    "policy_review_strict": "handlers.policy_review_strict",
    "policy_review": "handlers.policy_review",
    "deck_help": "handlers.deck_help",
    "community_mod": "handlers.community_mod",
    "general": "handlers.general",
}

def dispatch(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    state = state or {}

    route = decision["route"]

    # Optional: pass signals if you later store them in decision metadata
    # For now we evaluate based on policy_hits only.
    policy_hits = decision.get("policy_hits", [])
    policy_decision = evaluate_policy(route=route, policy_hits=policy_hits, signals=decision.get("signals", []))

    # Enforce route if policy engine says so
    if policy_decision.enforced_route:
        route = str(policy_decision.enforced_route)
        decision["route"] = route
        decision["policy_action"] = policy_decision.action
        decision["policy_severity"] = policy_decision.severity
        decision["policy_reasons"] = policy_decision.reasons
    else:
        decision["policy_action"] = policy_decision.action
        decision["policy_severity"] = policy_decision.severity
        decision["policy_reasons"] = policy_decision.reasons

    module_path = ROUTE_TO_HANDLER.get(route, "handlers.general")
    mod = import_module(module_path)
    out = mod.run(text=text, decision=decision, state=state)

    # Attach policy outputs to handler metadata
    out.metadata = dict(out.metadata or {})
    out.metadata["policy"] = {
        "action": policy_decision.action,
        "severity": policy_decision.severity,
        "reasons": policy_decision.reasons,
        "enforced_route": policy_decision.enforced_route,
    }
    return out