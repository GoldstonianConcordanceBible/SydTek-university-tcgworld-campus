from __future__ import annotations
import json
import sys
from pathlib import Path

from config.load_config import load_config
from routing.router import route_text

def main() -> int:
    cfg = load_config()

    text = ""
    if not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:]).strip()

    if not text:
        print("Usage: echo 'text' | python cli.py\n   or: python cli.py 'text to route'")
        return 2

    decision = route_text(
        text=text,
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=cfg.policy_enabled,
        embed_enabled=cfg.embed_enabled,
        embed_model_name=cfg.embed_model_name,
        embed_threshold=cfg.embed_threshold,
        embed_top_k=cfg.embed_top_k,
    )

    print(json.dumps(decision.to_dict(), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())