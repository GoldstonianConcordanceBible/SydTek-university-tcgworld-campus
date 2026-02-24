from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, List

from routing.tokenize import tokenize
from routing.regex_rules import find_policy_hits
from routing.embed_router import EmbeddingRouter, RouteScore

@dataclass
class RouteDecision:
    route: str
    reason: str
    policy_hits: int
    embedding: Optional[RouteScore] = None

DEFAULT_ROUTE = "general"

def route_text(
    text: str,
    policy_phrase_dir: Path,
    use_embeddings: bool = False,
    embed_threshold: float = 0.35,
) -> RouteDecision:
    t = tokenize(text)

    # 1) Policy phrase scan (hard signals)
    hits = find_policy_hits(t.normalized, policy_phrase_dir)

    if hits:
        # Example routing logic: route to a stricter handler
        categories = sorted({h.category for h in hits})
        return RouteDecision(
            route="policy_review",
            reason=f"Policy phrase hits: {categories}",
            policy_hits=len(hits),
        )

    # 2) Optional semantic routing (soft signals)
    if use_embeddings:
        router = EmbeddingRouter()
        router.build_routes({
            "tcg_trading": [
                "price prediction for a card",
                "should i buy this card now",
                "is this card a good investment",
                "profit from flipping cards"
            ],
            "community_mod": [
                "harassment report",
                "ban appeal",
                "rules enforcement",
                "toxicity in chat"
            ],
            "deck_help": [
                "optimize my deck",
                "best combo for this archetype",
                "sideboard choices",
                "matchup advice"
            ]
        })
        best = router.best_route(t.normalized, threshold=embed_threshold)
        if best:
            return RouteDecision(
                route=best.route,
                reason=f"Embedding similarity route={best.route} score={best.score:.3f}",
                policy_hits=0,
                embedding=best,
            )

    # 3) Default
    return RouteDecision(route=DEFAULT_ROUTE, reason="No policy hits; no strong semantic route", policy_hits=0)