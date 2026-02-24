from pathlib import Path
from routing.router import route_text

def test_routes_to_policy_review():
    d = route_text("I promise you guaranteed profit", Path("policy/phrase_lists"))
    assert d.route == "policy_review"
    assert d.policy_hits > 0