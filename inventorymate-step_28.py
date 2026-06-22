# === Stage 28: Add overdue item detection based on due dates ===
# Project: InventoryMate
from datetime import date, timedelta
from typing import List, Optional

def get_overdue_items(items: List[dict], days_threshold: int = 30) -> List[dict]:
    today = date.today()
    overdue = []
    for item in items:
        if 'warranty_expiry' in item and isinstance(item['warranty_expiry'], str):
            try:
                expiry_date = datetime.strptime(item['warranty_expiry'], '%Y-%m-%d').date()
                days_left = (expiry_date - today).days
                if days_left < 0:
                    overdue.append({**item, 'status': 'overdue', 'days_overdue': abs(days_left)})
            except ValueError:
                continue
    return overdue
