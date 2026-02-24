from pathlib import Path
from config.load_config import load_config
from routing.session_memory import RoutingMemory
from routing.router_with_memory import route_text_with_memory

def test_memory_stabilizes_default_route():
    cfg = load_config("config/config.yml")
    mem = RoutingMemory(maxlen=12)

    # Seed memory
    for _ in range(3):
        d = route_text_with_memory(
            "help me optimize my deck",
            mem,
            default_route=cfg.default_route,
            policy_phrase_dir=Path(cfg.policy_phrase_dir),
            policy_enabled=False,
            embed_enabled=False,
        )
        d.route = "deck_help"
        mem.add(d.route, d.reason)

    # Now send something ambiguous that would default
    d2 = route_text_with_memory(
        "what should I do next?",
        mem,
        default_route=cfg.default_route,
        policy_phrase_dir=Path(cfg.policy_phrase_dir),
        policy_enabled=False,
        embed_enabled=False,
    )
    assert d2.route == "deck_help"