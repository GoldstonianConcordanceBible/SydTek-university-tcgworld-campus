from __future__ import annotations
import hashlib
import json
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Optional

from accountability.hash import canonical_json, sha256_hex

def content_hash(mirror: str, water: str, fire: str) -> str:
    canon = canonical_json({"mirror": mirror, "water": water, "fire": fire})
    return sha256_hex(canon)

@dataclass
class Bundle:
    bundle_version: str
    created_unix: int
    decision_hash: str
    content_hash: str
    route: str
    policy_action: str
    policy_severity: float
    approval: Dict[str, Any]
    decision: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

def export_bundle(
    decision_hash_hex: str,
    decision: Dict[str, Any],
    mirror: str,
    water: str,
    fire: str,
    approval: Dict[str, Any],
    out_path: str = "accountability/bundles/latest.bundle.json",
) -> Dict[str, Any]:
    b = Bundle(
        bundle_version="1.0",
        created_unix=int(time.time()),
        decision_hash=decision_hash_hex,
        content_hash=content_hash(mirror, water, fire),
        route=str(decision.get("route", "unknown")),
        policy_action=str(decision.get("policy_action", "allow")),
        policy_severity=float(decision.get("policy_severity", 0.0)),
        approval=approval,
        decision=decision,
    )

    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(b.to_dict(), indent=2), encoding="utf-8")
    return b.to_dict()