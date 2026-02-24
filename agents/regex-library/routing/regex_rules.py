from __future__ import annotations
import regex as re
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class MatchHit:
    category: str
    phrase: str
    start: int
    end: int

def load_phrase_list(path: Path) -> List[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    phrases = data.get("phrases", [])
    return [p.strip().lower() for p in phrases if isinstance(p, str) and p.strip()]

def compile_phrases_to_regex(phrases: List[str]) -> re.Pattern:
    """
    Build a regex that matches any phrase as a whole-phrase-ish match.
    We allow flexible whitespace in phrases: 'risk free' matches 'risk   free'.
    """
    escaped = []
    for p in phrases:
        parts = [re.escape(x) for x in p.split()]
        if len(parts) == 1:
            escaped.append(parts[0])
        else:
            escaped.append(r"(?:%s)" % r"\s+".join(parts))

    # Word boundary-ish on both sides where reasonable
    # Use \b for latin scripts; for general Unicode, we keep it simple:
    pattern = r"(?<!\p{L})(%s)(?!\p{L})" % "|".join(escaped)
    return re.compile(pattern, flags=re.IGNORECASE | re.UNICODE)

def load_all_policy_regex(policy_dir: Path) -> Dict[str, Tuple[List[str], re.Pattern]]:
    out: Dict[str, Tuple[List[str], re.Pattern]] = {}
    for yml in policy_dir.glob("*.yml"):
        category = yml.stem
        phrases = load_phrase_list(yml)
        if phrases:
            out[category] = (phrases, compile_phrases_to_regex(phrases))
    return out

def find_policy_hits(text: str, policy_dir: Path) -> List[MatchHit]:
    rules = load_all_policy_regex(policy_dir)
    hits: List[MatchHit] = []
    for category, (phrases, rx) in rules.items():
        for m in rx.finditer(text):
            hits.append(MatchHit(category=category, phrase=m.group(1), start=m.start(1), end=m.end(1)))
    return hits