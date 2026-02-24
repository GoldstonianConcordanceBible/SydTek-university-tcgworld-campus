import json
import pathlib
import sys

def validate_jsonl(path: pathlib.Path) -> list[str]:
    errors = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if not isinstance(obj, dict):
                errors.append(f"{path}:{i} -> not a JSON object")
        except Exception as e:
            errors.append(f"{path}:{i} -> {e}")
    return errors

def main() -> int:
    roots = [pathlib.Path("datasets"), pathlib.Path("tests/suites")]
    errors = []
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*.jsonl"):
            errors.extend(validate_jsonl(p))

    if errors:
        print("JSONL VALIDATION FAILED:\n" + "\n".join(errors[:200]))
        print(f"\nTotal errors: {len(errors)}")
        return 1

    print("JSONL VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())