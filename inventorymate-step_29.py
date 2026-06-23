# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: InventoryMate
from datetime import datetime, timedelta
import json
from typing import List, Dict, Any

def get_upcoming_items(data: Dict[str, Any], days_ahead: int = 7) -> List[Dict[str, Any]]:
    """Return items with warranties expiring or maintenance due within specified days."""
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).date()
    upcoming = []
    
    for item in data.get("items", []):
        warranty_expiry = None
        if "warranty" in item and item["warranty"]:
            try:
                expiry_str = item["warranty"].get("expiry_date") or item["warranty"].get("end_date")
                if expiry_str:
                    warranty_expiry = datetime.strptime(expiry_str, "%Y-%m-%d").date()
            except ValueError:
                pass
        
        maintenance_due = None
        if "maintenance" in item and item["maintenance"]:
            try:
                due_str = item["maintenance"].get("due_date") or item["maintenance"].get("next_check")
                if due_str:
                    maintenance_due = datetime.strptime(due_str, "%Y-%m-%d").date()
            except ValueError:
                pass
        
        target_date = warranty_expiry or maintenance_due
        if target_date and now <= target_date <= cutoff:
            item_copy = dict(item)
            item_copy["alert_type"] = "warranty_expiring" if warranty_expiry else "maintenance_due"
            item_copy["days_left"] = (target_date - now).days
            upcoming.append(item_copy)
    
    return sorted(upcoming, key=lambda x: x.get("days_left", 999))

def format_alert_message(items: List[Dict[str, Any]], days_ahead: int = 7) -> str:
    """Generate a human-readable alert summary for upcoming items."""
    if not items:
        return f"No alerts within the next {days_ahead} days."
    
    lines = [f"InventoryMate Alerts (Next {days_ahead} Days):"]
    now_str = datetime.now().strftime("%Y-%m-%d")
    
    for item in items[:5]:  # Limit to top 5 alerts
        name = item.get("name", "Unknown Item")
        alert_type = item.get("alert_type", "")
        days_left = item.get("days_left", "?")
        
        if alert_type == "warranty_expiring":
            lines.append(f"⚠️ {name}: Warranty expires in {days_left} day(s).")
        elif alert_type == "maintenance_due":
            lines.append(f"🔧 {name}: Maintenance due in {days_left} day(s).")
    
    if len(items) > 5:
        lines[-1] = f"{lines[-1]} ... and {len(items) - 5} more items."
    
    return "\n".join(lines)

# Example usage (uncomment to test):
# data = {"items": [{"name": "Laptop", "warranty": {"expiry_date": "2024-12-31"}}]}
# alerts = get_upcoming_items(data, days_a
