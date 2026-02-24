from __future__ import annotations
from typing import Dict, Any, Optional
from handlers.base import HandlerOutput

def run(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    hits = decision.get("policy_hits", [])

    mirror = "I’m seeing wording that sounds like certainty/guarantee + money outcome framing."
    water = {
        "policy_hits_count": len(hits),
        "categories": sorted({h["category"] for h in hits}) if hits else [],
        "why_it_matters": "Claims of guaranteed profit or risk-free outcomes can mislead people."
    }
    fire = (
        "Let’s rephrase safely:\n"
        "- Focus on uncertainty + risk\n"
        "- Use factual, checkable info (prices, comps, liquidity)\n"
        "- Offer scenarios instead of promises\n"
        "If you paste the exact line you want to publish, I’ll rewrite it to remove guarantee/manipulation language."
    )

    return HandlerOutput(
        route="policy_review_strict",
        mirror=mirror,
        water=str(water),
        fire=fire,
        metadata={"policy_hits": hits}
    )