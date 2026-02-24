from dataclasses import dataclass
from typing import Optional

@dataclass
class EmbedRouteResult:
    route: str
    confidence: float
    evidence: Optional[str] = None

def route_with_embeddings(_text: str) -> Optional[EmbedRouteResult]:
    """
    Placeholder for optional embedding-based routing.
    Returns None by default so system falls back to regex/taxonomy.
    """
    return None