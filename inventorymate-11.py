# === Stage 11: Add JSON export for the current application state ===
# Project: InventoryMate
def export_to_json(data, filename="inventory.json"):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Exported {len(data)} items to {filename}")

def export_to_csv(data, filename="inventory.csv"):
    import csv
    if not data:
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Exported {len(data)} items to {filename}")
