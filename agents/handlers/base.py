from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, Protocol, Optional

@dataclass
class HandlerOutput:
    route: str
    mirror: str
    water: str
    fire: str
    metadata: Dict[str, Any]

class Handler(Protocol):
    def run(self, text: str, decision: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> HandlerOutput:
        ...