from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict
from pathlib import Path
import yaml

@dataclass
class RoutingConfig:
    default_route: str
    policy_enabled: bool
    policy_phrase_dir: str
    embed_enabled: bool
    embed_model_name: str
    embed_threshold: float
    embed_top_k: int

def load_config(path: str = "config/config.yml") -> RoutingConfig:
    p = Path(path)
    data: Dict[str, Any] = yaml.safe_load(p.read_text(encoding="utf-8"))

    routing = data.get("routing", {})
    policy = routing.get("policy_scan", {})
    emb = routing.get("embeddings", {})

    return RoutingConfig(
        default_route=str(routing.get("default_route", "general")),
        policy_enabled=bool(policy.get("enabled", True)),
        policy_phrase_dir=str(policy.get("phrase_dir", "policy/phrase_lists")),
        embed_enabled=bool(emb.get("enabled", False)),
        embed_model_name=str(emb.get("model_name", "all-MiniLM-L6-v2")),
        embed_threshold=float(emb.get("threshold", 0.35)),
        embed_top_k=int(emb.get("top_k", 3)),
    )