from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except Exception:
    SentenceTransformer = None

@dataclass
class RouteScore:
    route: str
    score: float

def cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b)) + 1e-12
    return float(np.dot(a, b) / denom)

class EmbeddingRouter:
    """
    Optional semantic routing. If sentence-transformers isn't installed,
    you can skip using this class.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        if SentenceTransformer is None:
            raise RuntimeError("sentence-transformers not installed")
        self.model = SentenceTransformer(model_name)
        self.route_vectors: Dict[str, np.ndarray] = {}

    def build_routes(self, route_exemplars: Dict[str, List[str]]) -> None:
        """
        route_exemplars: { "route_name": ["example phrase 1", "example 2", ...] }
        """
        for route, examples in route_exemplars.items():
            vecs = self.model.encode(examples, normalize_embeddings=True)
            mean_vec = np.mean(vecs, axis=0)
            self.route_vectors[route] = mean_vec / (np.linalg.norm(mean_vec) + 1e-12)

    def score(self, text: str, top_k: int = 3) -> List[RouteScore]:
        q = self.model.encode([text], normalize_embeddings=True)[0]
        scores = [RouteScore(route=r, score=cosine(q, v)) for r, v in self.route_vectors.items()]
        scores.sort(key=lambda x: x.score, reverse=True)
        return scores[:top_k]

    def best_route(self, text: str, threshold: float = 0.35) -> Optional[RouteScore]:
        top = self.score(text, top_k=1)[0]
        return top if top.score >= threshold else None