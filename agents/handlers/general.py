from __future__ import annotations
from typing import Dict, Any, Optional
from handlers.base import HandlerOutput

def run(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    mirror = "General question / no special policy or domain lane detected."
    water = "If you share what ‘TCG World’ refers to (game, app, marketplace), I can respond precisely."
    fire = "Give me: platform + your goal (play, trade, collect, build community) and I’ll produce a next-action plan."
    return HandlerOutput(route="general", mirror=mirror, water=water, fire=fire, metadata={})