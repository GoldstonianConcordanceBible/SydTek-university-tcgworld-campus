from __future__ import annotations
from pathlib import Path
from typing import Optional, List, Dict, Any

from routing.tokenize import tokenize
from routing.regex_rules import find_policy_hits
from routing.embed_router import EmbeddingRouter
from routing.contracts import RouteDecision, PolicyHit, EmbeddingDecision

def route_text(
    text: str,
    default_route: str,
    policy_phrase_dir: Path,
    policy_enabled: bool = True,
    embed_enabled: bool = False,
    embed_model_name: str = "all-MiniLM-L6-v2",
    embed_threshold: float = 0.35,
    embed_top_k: int = 3,
) -> RouteDecision:
    t = tokenize(text)

    # 1) Policy scan (hard gate)
    if policy_enabled:
        hits_raw = find_policy_hits(t.normalized, policy_phrase_dir)
        hits: List[PolicyHit] = [
            PolicyHit(category=h.category, phrase=h.phrase, start=h.start, end=h.end)
            for h in hits_raw
        ]
        if hits:
            cats = sorted({h.category for h in hits})
            return RouteDecision(
                route="policy_review",
                reason=f"Policy phrase hits: {cats}",
                policy_hits=hits,
                embedding=None,
            )

    # 2) Embedding router (soft route)
    if embed_enabled:
        router = EmbeddingRouter(model_name=embed_model_name)
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

        scores = router.score(t.normalized, top_k=embed_top_k)
        best = scores[0] if scores else None
        if best and best.score >= embed_threshold:
            return RouteDecision(
                route=best.route,
                reason=f"Embedding similarity route={best.route} score={best.score:.3f}",
                policy_hits=[],
                embedding=EmbeddingDecision(
                    route=best.route,
                    score=best.score,
                    top_k=[{"route": s.route, "score": s.score} for s in scores]
                ),
            )

    # 3) Default
    return RouteDecision(
        route=default_route,
        reason="Default route (no policy hits; no strong embedding route)",
        policy_hits=[],
        embedding=None,
    )