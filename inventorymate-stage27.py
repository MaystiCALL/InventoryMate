# === Stage 27: Add monthly summary calculations ===
# Project: InventoryMate
from datetime import datetime, timedelta
def calculate_monthly_summary(inventory):
    today = datetime.now()
    current_month_start = today.replace(day=1)
    current_month_end = (current_month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    monthly_stats = {"total_value": 0, "items_count": 0, "expired_warranties": [], "upcoming_expirations": []}
    for item in inventory:
        if current_month_start <= datetime.strptime(item["purchase_date"], "%Y-%m-%d") < current_month_end:
            monthly_stats["total_value"] += float(item.get("price", 0))
            monthly_stats["items_count"] += 1
        warranty_expiry = datetime.strptime(item.get("warranty_expiry", "9999-12-31"), "%Y-%m-%d")
        if warranty_expiry < current_month_end:
            monthly_stats["expired_warranties"].append({"item": item["name"], "days_overdue": (current_month_end - warranty_expiry).days})
        elif warranty_expiry <= current_month_end + timedelta(days=30):
            monthly_stats["upcoming_expirations"].append({"item": item["name"], "expiry_date": warranty_expiry.strftime("%Y-%m-%d")})
    return monthly_stats
