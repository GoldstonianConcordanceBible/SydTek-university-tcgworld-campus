from __future__ import annotations
from dataclasses import dataclass
from typing import Deque, Optional
from collections import deque

@dataclass
class MemoryItem:
    route: str
    reason: str

class RoutingMemory:
    def __init__(self, maxlen: int = 12):
        self.buf: Deque[MemoryItem] = deque(maxlen=maxlen)

    def add(self, route: str, reason: str) -> None:
        self.buf.append(MemoryItem(route=route, reason=reason))

    def dominant_route(self, min_count: int = 3) -> Optional[str]:
        counts = {}
        for item in self.buf:
            counts[item.route] = counts.get(item.route, 0) + 1
        if not counts:
            return None
        route, count = max(counts.items(), key=lambda kv: kv[1])
        return route if count >= min_count else None