from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Any
import yaml

def load_exemplars(path: str = "routing/exemplars.yml") -> Dict[str, List[str]]:
    p = Path(path)
    data: Dict[str, Any] = yaml.safe_load(p.read_text(encoding="utf-8"))
    routes = data.get("routes", {})
    out: Dict[str, List[str]] = {}
    for route_name, payload in routes.items():
        examples = payload.get("examples", [])
        if isinstance(examples, list):
            out[route_name] = [str(x) for x in examples if str(x).strip()]
    return out