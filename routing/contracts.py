from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional

@dataclass
class PolicyHit:
    category: str
    phrase: str
    start: int
    end: int

@dataclass
class EmbeddingDecision:
    route: str
    score: float
    top_k: Optional[List[Dict[str, Any]]] = None

@dataclass
class RouteDecision:
    route: str
    reason: str
    policy_hits: List[PolicyHit]
    embedding: Optional[EmbeddingDecision] = None
    version: str = "1.0"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)