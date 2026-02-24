from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
from rapidfuzz import fuzz

@dataclass
class FuzzyHit:
    category: str
    phrase: str
    matched_text: str
    score: float
    span: Tuple[int, int]

def fuzzy_find_phrases(
    text: str,
    category: str,
    phrases: List[str],
    window_chars: int = 64,
    threshold: float = 90.0,
) -> List[FuzzyHit]:
    """
    Sliding-window fuzzy search over text. This catches typos like:
    'guarenteed' ~ 'guaranteed'
    """
    hits: List[FuzzyHit] = []
    t = text.lower()

    # Generate windows (start every ~window/2 chars for coverage)
    step = max(8, window_chars // 2)
    for start in range(0, max(1, len(t) - 1), step):
        end = min(len(t), start + window_chars)
        chunk = t[start:end]

        for p in phrases:
            p2 = p.lower()
            score = float(fuzz.partial_ratio(p2, chunk))
            if score >= threshold:
                # approximate span: we don't know exact indices from fuzzy match,
                # but we can return the window span for downstream review.
                hits.append(FuzzyHit(
                    category=category,
                    phrase=p,
                    matched_text=chunk,
                    score=score,
                    span=(start, end),
                ))

    # Deduplicate overlapping hits (keep best score per phrase per overlapping window)
    hits.sort(key=lambda h: (h.category, h.phrase, -h.score, h.span[0]))
    dedup: List[FuzzyHit] = []
    for h in hits:
        if not dedup:
            dedup.append(h)
            continue
        prev = dedup[-1]
        overlap = not (h.span[1] <= prev.span[0] or h.span[0] >= prev.span[1])
        if h.category == prev.category and h.phrase == prev.phrase and overlap:
            # keep best (already sorted)
            continue
        dedup.append(h)

    return dedup