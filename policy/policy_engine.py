from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import yaml

@dataclass
class PolicyDecision:
    action: str                 # allow | rewrite | block | escalate
    severity: float             # 0..1
    reasons: List[str]
    enforced_route: Optional[str] = None

def _load_yaml(path: Path) -> Dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))

def evaluate_policy(
    route: str,
    policy_hits: List[Dict[str, Any]],
    signals: Optional[List[Dict[str, Any]]] = None,
    policy_file: str = "policy/route_policies.yml",
) -> PolicyDecision:
    cfg = _load_yaml(Path(policy_file))
    routes = cfg.get("routes", {})
    cats_cfg = cfg.get("categories", {})
    global_cfg = cfg.get("global", {})
    escalators = cfg.get("context_escalators", {})

    allowed_actions = routes.get(route, {}).get("allowed_actions", ["allow"])

    # Base: sum severities by category presence (max-based for simplicity)
    categories_present = sorted({h.get("category") for h in policy_hits if h.get("category")})
    severity = float(global_cfg.get("default_severity", 0.0))
    reasons: List[str] = []

    for cat in categories_present:
        base = float(cats_cfg.get(cat, {}).get("base_severity", 0.25))
        severity = max(severity, base)
        reasons.append(f"category={cat} base_severity={base}")

    action = str(global_cfg.get("default_action", "allow"))

    # Default action by highest category (if any)
    if categories_present:
        # Pick the most severe category for default action
        top_cat = max(categories_present, key=lambda c: float(cats_cfg.get(c, {}).get("base_severity", 0.0)))
        action = str(cats_cfg.get(top_cat, {}).get("default_action", "rewrite"))
        reasons.append(f"default_action_from={top_cat}:{action}")

    enforced_route: Optional[str] = None

    # Apply context escalators (signals are produced by router/context_rules)
    signals = signals or []
    signal_names = {s.get("name") for s in signals if s.get("name")}

    for esc_name, esc in escalators.items():
        required = set(esc.get("categories_required", []))
        sig = str(esc.get("signal", ""))

        if required.issubset(set(categories_present)) and sig in signal_names:
            bump = float(esc.get("severity_bump", 0.0))
            severity = clamp01(severity + bump)
            reasons.append(f"escalator={esc_name} bump={bump} via_signal={sig}")

            enforced_route = esc.get("force_route")
            forced_action = esc.get("force_action")
            if forced_action:
                action = str(forced_action)
                reasons.append(f"forced_action={action}")

    # Enforce route allowed actions
    if action not in allowed_actions:
        # escalate if not allowed, else rewrite, else allow as fallback
        if "escalate" in allowed_actions:
            reasons.append(f"action={action} not allowed for route={route}; coercing->escalate")
            action = "escalate"
        elif "rewrite" in allowed_actions:
            reasons.append(f"action={action} not allowed for route={route}; coercing->rewrite")
            action = "rewrite"
        else:
            reasons.append(f"action={action} not allowed for route={route}; coercing->allow")
            action = "allow"

    return PolicyDecision(action=action, severity=severity, reasons=reasons, enforced_route=enforced_route)