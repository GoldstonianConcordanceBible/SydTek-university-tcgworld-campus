import re
from dataclasses import dataclass
from typing import Optional, Pattern

@dataclass(frozen=True)
class RegexRule:
    name: str
    pattern: Pattern[str]
    route: str
    confidence: float = 0.65
    notes: Optional[str] = None

DEFAULT_RULES = [
    RegexRule(
        name="crypto_guarantee_bait",
        pattern=re.compile(r"\b(guarantee|guaranteed|risk[-\s]?free|no risk)\b", re.IGNORECASE),
        route="policy_finance_guardrails",
        confidence=0.9,
        notes="Triggers finance safety route."
    ),
    RegexRule(
        name="credential_request",
        pattern=re.compile(r"\b(badge|credential|certificate|attestation)\b", re.IGNORECASE),
        route="credentialing",
        confidence=0.8
    ),
]