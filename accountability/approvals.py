from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional
import time

@dataclass
class ApprovalRecord:
    decision_hash: str
    approved: bool
    approved_by: str               # e.g., "human:justin" or "agent:gemach-data-1"
    approval_reason: str
    timestamp_unix: int
    signature: Optional[str] = None  # placeholder for future signing (ed25519, wallet sig, etc.)
    policy_version: Optional[str] = None
    router_version: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

def new_approval(
    decision_hash: str,
    approved: bool,
    approved_by: str,
    approval_reason: str,
    signature: Optional[str] = None,
    policy_version: Optional[str] = None,
    router_version: Optional[str] = None,
) -> ApprovalRecord:
    return ApprovalRecord(
        decision_hash=decision_hash,
        approved=approved,
        approved_by=approved_by,
        approval_reason=approval_reason,
        timestamp_unix=int(time.time()),
        signature=signature,
        policy_version=policy_version,
        router_version=router_version,
    )