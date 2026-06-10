# === Stage 4: Implement create operations for the primary records ===
# Project: InventoryMate
from datetime import date, timedelta
import random

def create_room(name: str) -> dict:
    return {"id": f"room_{random.randint(1000, 9999)}", "name": name, "created_at": date.today().isoformat()}

def create_item(room_id: str, name: str, purchase_date: str = None, warranty_months: int = 0) -> dict:
    if not purchase_date:
        purchase_date = (date.today() - timedelta(days=random.randint(30, 365))).isoformat()
    return {
        "id": f"item_{random.randint(10000, 99999)}",
        "room_id": room_id,
        "name": name,
        "purchase_date": purchase_date,
        "warranty_months": warranty_months,
        "tags": [],
        "notes": ""
    }

def create_tag(name: str) -> dict:
    return {"id": f"tag_{random.randint(100, 999)}", "name": name.lower().replace(" ", "_")}

def create_warranty(item_id: str, start_date: str = None, end_date: str = None) -> dict:
    if not start_date:
        purchase_str = item.get("purchase_date", date.today().isoformat())
        start_date = purchase_str
    if not end_date and item.get("warranty_months"):
        months = item["warranty_months"]
        d = date.fromisoformat(start_date)
        end_date = (d + timedelta(days=30*months)).isoformat()
    else:
        end_date = end_date or start_date
    return {
        "id": f"war_{random.randint(1000, 9999)}",
        "item_id": item_id,
        "start_date": start_date,
        "end_date": end_date
    }
