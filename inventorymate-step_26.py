# === Stage 26: Add weekly summary calculations ===
# Project: InventoryMate
from datetime import datetime, timedelta
def calculate_weekly_summary(inventory):
    now = datetime.now()
    week_start = (now - timedelta(days=now.weekday())).date()
    week_end = week_start + timedelta(days=6)
    summary = {"week": f"{week_start} - {week_end}", "total_items": 0, "rooms_count": set()}
    for room in inventory.values():
        for item in room.get("items", []):
            if item.get("status") == "active" and item.get("purchase_date"):
                summary["total_items"] += 1
                summary["rooms_count"].add(item.get("room"))
    return {**summary, "rooms_count": len(summary["rooms_count"]), "coverage_rate": round(100 * summary["total_items"] / max(sum(v.get("count", 0) for v in inventory.values()), 1), 2)}
