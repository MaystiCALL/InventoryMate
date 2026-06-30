# === Stage 42: Add CSV export without external dependencies ===
# Project: InventoryMate
def export_to_csv(items, filename="inventory.csv"):
    import csv
    if not items: return False
    headers = ["id", "name", "room", "tags", "purchase_date", "warranty_end"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for item in items:
            row = {h: str(item.get(h, "")) for h in headers}
            writer.writerow(row)
    return True
