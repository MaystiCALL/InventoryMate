# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: InventoryMate
import json, sys

def load_inventory(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Error: Root element must be a JSON array.", file=sys.stderr)
            sys.exit(1)
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                print(f"Error: Item at index {i} is not an object.", file=sys.stderr)
                sys.exit(1)
        return data
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON syntax - {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: File not found.", file=sys.stderr)
        sys.exit(1)
