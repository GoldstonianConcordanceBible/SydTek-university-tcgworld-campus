from pathlib import Path
from routing.regex_rules import find_policy_hits

def test_guarantee_hits():
    policy_dir = Path("policy/phrase_lists")
    hits = find_policy_hits("This is guaranteed to work. Risk free.", policy_dir)
    assert any(h.category == "guarantees" for h in hits)