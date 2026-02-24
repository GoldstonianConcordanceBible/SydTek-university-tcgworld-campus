from __future__ import annotations
from typing import Dict, Any, Optional
from handlers.base import HandlerOutput

def run(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    mirror = "You’re asking for deck optimization and matchup improvement."
    water = (
        "To answer well, I need:\n"
        "- Format/ruleset\n"
        "- Your deck list\n"
        "- Your local meta (top 3 decks)\n"
        "- What you keep losing to (control, aggro, combo)\n"
    )
    fire = (
        "Drop your deck list (paste or screenshot text). I’ll respond with:\n"
        "1) 3 core problems\n"
        "2) 5–10 card swaps\n"
        "3) Sideboard plan + mulligan notes\n"
        "4) A ‘Mirror → Water → Fire’ recap for your training agents"
    )
    return HandlerOutput(route="deck_help", mirror=mirror, water=water, fire=fire, metadata={})