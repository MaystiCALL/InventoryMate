# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: InventoryMate
import json
from datetime import datetime, timedelta
from typing import Optional

class Item:
    def __init__(self, name: str, room: str, purchase_date: str, warranty_months: int = 12):
        self.name = name
        self.room = room
        self.purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        self.warranty_months = warranty_months
        self.tags: list[str] = []

    def is_warranty_active(self) -> bool:
        today = datetime.now()
        expiry = self.purchase_date + timedelta(days=self.warranty_months * 30)
        return today < expiry

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "room": self.room,
            "purchase_date": self.purchase_date.strftime("%Y-%m-%d"),
            "warranty_months": self.warranty_months,
            "tags": self.tags,
            "warranty_active": self.is_warranty_active()
        }

class Inventory:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, name: str, room: str, purchase_date: str, warranty_months: int = 12, tags: Optional[list[str]] = None):
        item = Item(name, room, purchase_date, warranty_months)
        if tags:
            item.tags.extend(tags)
        self.items.append(item)

    def search(self, query: str) -> list[Item]:
        q = query.lower()
        return [i for i in self.items if q in i.name.lower() or q in i.room.lower()]

    def export_json(self, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([i.to_dict() for i in self.items], f, indent=2)

# Demo dataset
inv = Inventory()
inv.add_item("Laptop Pro", "Office", "2023-01-15", 24, ["work", "electronics"])
inv.add_item("Coffee Maker", "Kitchen", "2022-06-10", 12)
inv.add_item("Gaming Chair", "Living Room", "2023-03-20", 36, ["furniture", "ergonomic"])

# Save demo data
inv.export_json("inventory_demo.json")
