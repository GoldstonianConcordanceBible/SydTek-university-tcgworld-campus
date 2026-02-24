from __future__ import annotations
from typing import Dict, Any, Optional
from handlers.base import HandlerOutput

def run(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    hits = decision.get("policy_hits", [])
    mirror = "I’m noticing policy-sensitive phrasing (pressure/guarantee/manipulation style)."
    water = f"Hits detected: {len(hits)} | categories={sorted({h['category'] for h in hits}) if hits else []}"
    fire = (
        "Safer alternatives:\n"
        "- Replace certainty words with probabilities (might/could)\n"
        "- Remove pressure language (act now / last chance)\n"
        "- Add a clear disclaimer: no guarantees\n"
        "Want me to rewrite your message into a compliant version?"
    )
    return HandlerOutput(route="policy_review", mirror=mirror, water=water, fire=fire, metadata={"policy_hits": hits})