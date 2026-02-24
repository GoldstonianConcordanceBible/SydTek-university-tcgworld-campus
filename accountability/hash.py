from __future__ import annotations
import hashlib
import json
from typing import Any, Dict

def canonical_json(obj: Dict[str, Any]) -> str:
    # stable ordering, no whitespace drift
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def decision_hash(decision_payload: Dict[str, Any]) -> str:
    """
    Hash only the decision contract (not full handler text),
    so it stays stable and comparable across versions.
    """
    canon = canonical_json(decision_payload)
    return sha256_hex(canon)