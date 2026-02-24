from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class ContextSignal:
    name: str
    evidence: List[str]
    span: Tuple[int, int]

def has_nearby_context(
    text: str,
    anchor_spans: List[Tuple[int, int]],
    context_terms: List[str],
    radius_chars: int = 120,
) -> List[ContextSignal]:
    """
    If any context term appears within radius_chars of an anchor span,
    return a signal describing it.
    """
    t = text.lower()
    signals: List[ContextSignal] = []

    for (a0, a1) in anchor_spans:
        left = max(0, a0 - radius_chars)
        right = min(len(t), a1 + radius_chars)
        window = t[left:right]

        found = []
        for term in context_terms:
            term_l = term.lower()
            if term_l in window:
                found.append(term)

        if found:
            signals.append(ContextSignal(
                name="money_context_near_policy_anchor",
                evidence=sorted(set(found)),
                span=(left, right),
            ))

    return signals