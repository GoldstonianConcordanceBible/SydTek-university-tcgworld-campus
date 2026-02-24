from __future__ import annotations
from pathlib import Path
from typing import Optional

from routing.router import route_text
from routing.session_memory import RoutingMemory
from routing.contracts import RouteDecision

def route_text_with_memory(
    text: str,
    mem: RoutingMemory,
    default_route: str,
    policy_phrase_dir: Path,
    **kwargs,
) -> RouteDecision:
    decision = route_text(
        text=text,
        default_route=default_route,
        policy_phrase_dir=policy_phrase_dir,
        **kwargs,
    )

    # If user has been consistently in a route (and current is default),
    # keep them in that lane to reduce drift.
    dom = mem.dominant_route(min_count=3)
    if dom and decision.route == default_route:
        decision.route = dom
        decision.reason = f"Memory-stabilized route={dom} (dominant in recent turns)"

    mem.add(decision.route, decision.reason)
    return decision