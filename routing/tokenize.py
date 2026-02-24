import re
from typing import List

_WORD_RE = re.compile(r"[A-Za-z0-9']+")

def simple_tokens(text: str) -> List[str]:
    """
    Minimal tokenizer used by routing. Keep deterministic and dependency-light.
    """
    return [t.lower() for t in _WORD_RE.findall(text or "")]