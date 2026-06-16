# === Stage 14: Add file load support with fallback demo data ===
# Project: InventoryMate
def load_or_demo():
    try:
        with open('inventory.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "rooms": ["Kitchen", "Living Room"],
            "items": [
                {"name": "Toaster", "room": "Kitchen", "warranty_end": "2025-12-31"},
                {"name": "Sofa", "room": "Living Room", "tags": ["furniture"]}
            ]
        }
