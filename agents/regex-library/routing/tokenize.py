from __future__ import annotations
import regex as re
from dataclasses import dataclass
from typing import List

# Unicode-aware word tokens + keep apostrophes inside words
TOKEN_RE = re.compile(r"\p{L}+(?:'\p{L}+)?|\p{N}+|[^\s]", re.UNICODE)

@dataclass(frozen=True)
class Tokenized:
    text: str
    tokens: List[str]
    normalized: str

def normalize(text: str) -> str:
    # Lowercase + collapse whitespace
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text: str) -> Tokenized:
    norm = normalize(text)
    toks = TOKEN_RE.findall(norm)
    return Tokenized(text=text, tokens=toks, normalized=norm)