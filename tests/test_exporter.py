from accountability.exporter import export_bundle

def test_export_bundle_writes_file(tmp_path):
    out_file = tmp_path / "bundle.json"
    b = export_bundle(
        decision_hash_hex="abc123",
        decision={"route": "general", "policy_action": "allow", "policy_severity": 0.0, "version": "1.0"},
        mirror="m", water="w", fire="f",
        approval={"approved": True},
        out_path=str(out_file),
    )
    assert b["decision_hash"] == "abc123"
    assert out_file.exists()