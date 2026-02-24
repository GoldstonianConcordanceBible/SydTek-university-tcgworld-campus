from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ActionResult:
    action: str
    output: Dict[str, Any]   # final payload

def apply_policy_action(payload: Dict[str, Any]) -> ActionResult:
    """
    payload must include metadata.policy.action
    """
    policy = (payload.get("metadata") or {}).get("policy") or {}
    action = str(policy.get("action", "allow"))

    if action == "allow":
        return ActionResult(action="allow", output=payload)

    if action == "rewrite":
        # For now, keep handler output; downstream can implement an automatic rewriter.
        payload["fire"] = (
            str(payload.get("fire", "")) +
            "\n\n[Rewrite Mode]\nPaste the exact sentence you want to publish and I’ll rewrite it to remove guarantee/pressure language."
        )
        return ActionResult(action="rewrite", output=payload)

    if action == "block":
        # Block: return safe refusal-style output (no details, no enabling)
        blocked = {
            "decision": payload.get("decision"),
            "mirror": "I can’t help produce or support content that implies guaranteed outcomes or manipulates people.",
            "water": "We can still make a safe version that’s factual, uncertainty-aware, and non-coercive.",
            "fire": "Share your goal and your draft line, and I’ll rewrite it in a compliant way.",
            "metadata": payload.get("metadata", {}),
        }
        return ActionResult(action="block", output=blocked)

    if action == "escalate":
        escalated = {
            "decision": payload.get("decision"),
            "mirror": "This needs review before it’s used publicly.",
            "water": "I can help you rewrite it safely, but I can’t assist with anything that bypasses rules or misleads people.",
            "fire": "Paste the exact copy + where it will be posted (marketplace listing, Discord, stream overlay), and I’ll produce a compliant rewrite + a safe disclaimer.",
            "metadata": payload.get("metadata", {}),
        }
        return ActionResult(action="escalate", output=escalated)

    # Unknown action => allow
    return ActionResult(action="allow", output=payload)