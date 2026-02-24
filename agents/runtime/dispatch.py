from __future__ import annotations
from importlib import import_module
from typing import Dict, Any, Optional

from handlers.base import HandlerOutput

ROUTE_TO_HANDLER = {
    "policy_review_strict": "handlers.policy_review_strict",
    "policy_review": "handlers.policy_review",
    "deck_help": "handlers.deck_help",
    "community_mod": "handlers.community_mod",
    "general": "handlers.general",
}

def dispatch(text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
    route = decision["route"]
    module_path = ROUTE_TO_HANDLER.get(route, "handlers.general")
    mod = import_module(module_path)
    return mod.run(text=text, decision=decision, state=state)