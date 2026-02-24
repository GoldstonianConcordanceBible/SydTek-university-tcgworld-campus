from __future__ import annotations
from pathlib import Path
from typing import List, Tuple

from routing.tokenize import tokenize
from routing.regex_rules import find_policy_hits, load_phrase_lists
from routing.fuzzy_match import fuzzy_find_phrases
from routing.context_rules import has_nearby_context
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

    # NEW knobs
    fuzzy_enabled: bool = True,
    fuzzy_threshold: float = 90.0,
    context_radius_chars: int = 120,
) -> RouteDecision:
    t = tokenize(text)

    # 1) Policy scan (regex + optional fuzzy)
    policy_hits: List[PolicyHit] = []
    anchor_spans: List[Tuple[int, int]] = []

    if policy_enabled:
        hits_raw = find_policy_hits(t.normalized, policy_phrase_dir)
        for h in hits_raw:
            policy_hits.append(PolicyHit(category=h.category, phrase=h.phrase, start=h.start, end=h.end))
            anchor_spans.append((h.start, h.end))

        if fuzzy_enabled:
            phrase_lists = load_phrase_lists(policy_phrase_dir)

            # Only fuzzy-check the highest-risk lists first
            for category in ("guarantees", "manipulation", "compliance"):
                phrases = phrase_lists.get(category, [])
                if not phrases:
                    continue
                fuzzy_hits = fuzzy_find_phrases(
                    text=t.normalized,
                    category=category,
                    phrases=phrases,
                    window_chars=64,
                    threshold=fuzzy_threshold,
                )
                for fh in fuzzy_hits:
                    # Represent fuzzy span as window span
                    s0, s1 = fh.span
                    policy_hits.append(PolicyHit(category=fh.category, phrase=fh.phrase, start=s0, end=s1))
                    anchor_spans.append((s0, s1))

        if policy_hits:
            # 2) Context escalation: guarantees + money context => "policy_review_strict"
            phrase_lists = load_phrase_lists(policy_phrase_dir)
            money_terms = phrase_lists.get("money_context", [])
            signals = has_nearby_context(
                text=t.normalized,
                anchor_spans=anchor_spans,
                context_terms=money_terms,
                radius_chars=context_radius_chars,
            )

            cats = sorted({h.category for h in policy_hits})
            if ("guarantees" in cats) and signals:
                return RouteDecision(
                    route="policy_review_strict",
                    reason=f"Guarantee + money-context proximity: evidence={signals[0].evidence[:6]}",
                    policy_hits=policy_hits,
                    embedding=None,
                )

            return RouteDecision(
                route="policy_review",
                reason=f"Policy hits: {cats}",
                policy_hits=policy_hits,
                embedding=None,
            )

    # 3) Embedding route (soft)
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

    return RouteDecision(
        route=default_route,
        reason="Default route",
        policy_hits=[],
        embedding=None,
    )