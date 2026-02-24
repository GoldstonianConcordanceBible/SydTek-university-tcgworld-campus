import json
import pathlib

def main() -> int:
    p = pathlib.Path(".zenodo.json")
    if not p.exists():
        print("No .zenodo.json found — skipping.")
        return 0

    raw = p.read_text(encoding="utf-8")
    try:
        json.loads(raw)
    except Exception as e:
        print("INVALID .zenodo.json — must be strict JSON (no comments).")
        print(f"Error: {e}")
        return 1

    print(".zenodo.json is valid JSON")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())