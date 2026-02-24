from pathlib import Path
from config.load_config import load_config
from routing.router import route_text

def test_fuzzy_catches_misspelling():
    cfg = load_config("config/config.yml")
    d = route_text(
        "This is guarenteed to work.",
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=True,
        embed_enabled=False,
        fuzzy_enabled=True,
        fuzzy_threshold=85.0,
    )
    assert d.route in ("policy_review", "policy_review_strict")
    assert len(d.policy_hits) > 0

def test_strict_escalation_guarantee_plus_money():
    cfg = load_config("config/config.yml")
    d = route_text(
        "Guaranteed profit if you buy now.",
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=True,
        embed_enabled=False,
        fuzzy_enabled=False,
    )
    assert d.route == "policy_review_strict"