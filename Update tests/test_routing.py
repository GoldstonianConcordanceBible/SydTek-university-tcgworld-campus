from pathlib import Path
from config.load_config import load_config
from routing.router import route_text

def test_config_loads():
    cfg = load_config("config/config.yml")
    assert cfg.default_route

def test_routes_to_policy_review():
    cfg = load_config("config/config.yml")
    d = route_text(
        "I promise guaranteed profit",
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=True,
        embed_enabled=False,
    )
    assert d.route == "policy_review"
    assert len(d.policy_hits) > 0