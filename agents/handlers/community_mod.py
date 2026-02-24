from __future__ import annotations
from typing import Dict, Any, Optional
from handlers.base import HandlerOutput

def run(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    mirror = "You’re reporting harassment / needing moderation help."
    water = (
        "Best practice steps:\n"
        "- Document the message (screenshots, timestamps)\n"
        "- Use in-app report tools\n"
        "- Block/mute if available\n"
        "- Escalate to mods with evidence"
    )
    fire = (
        "If you tell me the platform (Discord / in-game / Twitch / etc.), I’ll output:\n"
        "- Exact report flow\n"
        "- Moderator checklist\n"
        "- Template message to mods\n"
        "- Repeat-offender handling (warnings → temp mute → ban)"
    )
    return HandlerOutput(route="community_mod", mirror=mirror, water=water, fire=fire, metadata={})