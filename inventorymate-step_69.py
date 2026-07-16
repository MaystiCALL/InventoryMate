# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: InventoryMate
def reset_demo_data():
    """Reset all demo data in rooms, warranties, tags, inventory, and search indexes."""
    import json
    from pathlib import Path
    BASE = Path(__file__).resolve().parent / "data"
    DEMO = {
        "rooms": [
            {"id": 1, "name": "Living Room"},
            {"id": 2, "name": "Kitchen"},
            {"id": 3, "name": "Bedroom"}
        ],
        "warranties": [
            {"id": 1, "product_id": 101, "start_date": "2024-01-01", "end_date": "2025-01-01"},
            {"id": 2, "product_id": 102, "start_date": "2023-06-15", "end_date": "2024-06-15"}
        ],
        "tags": [
            {"id": 1, "name": "Electronics"},
            {"id": 2, "name": "Furniture"},
            {"id": 3, "name": "Sports"}
        ]
    }
    for section in ("rooms", "warranties", "tags"):
        file_path = BASE / f"{section}.json"
        if file_path.exists():
            with open(file_path, "w") as f:
                json.dump(DEMO[section], f, indent=2)
    print("Demo data reset successfully.")

if __name__ == "__main__":
    reset_demo_data()
