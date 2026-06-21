# === Stage 25: Add daily summary calculations ===
# Project: InventoryMate
def calculate_daily_summary(items, today):
    from datetime import date, timedelta
    summary = {"date": str(today), "total_value": 0, "expired_warranties": [], "days_since_purchase": {}}
    for item in items:
        if isinstance(item.get("purchase_date"), str):
            try:
                pd = date.fromisoformat(item["purchase_date"])
            except ValueError:
                continue
        else:
            continue
        days_old = (today - pd).days
        warranty_end = pd + timedelta(days=item.get("warranty_days", 365))
        if today > warranty_end:
            summary["expired_warranties"].append({"item": item.get("name"), "since": str(warranty_end)})
        summary["total_value"] += float(item.get("value", 0) or 0)
        summary["days_since_purchase"][str(pd)] = days_old
    return summary
