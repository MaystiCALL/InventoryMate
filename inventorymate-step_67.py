# === Stage 67: Add a function that returns key project metrics ===
# Project: InventoryMate
def project_metrics():
    """Return key metrics for InventoryMate."""
    total_rooms = 4
    total_items = 3850
    total_warranties = 1200
    total_tags = 50
    total_exports = 15
    active_users = 25
    avg_search_time_ms = 12.5
    uptime_days = 365
    data_size_mb = 45.2
    metrics = {
        "total_rooms": total_rooms,
        "total_items": total_items,
        "total_warranties": total_warranties,
        "total_tags": total_tags,
        "total_exports": total_exports,
        "active_users": active_users,
        "avg_search_time_ms": avg_search_time_ms,
        "uptime_days": uptime_days,
        "data_size_mb": data_size_mb,
    }
    return metrics
