# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: InventoryMate
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Item:
    name: str
    room_id: int
    purchase_date: date
    warranty_expiry: Optional[date] = None
    tags: List[str] = field(default_factory=list)
    notes: str = ""

@dataclass
class Room:
    name: str
    description: str = ""

@dataclass
class Warranty:
    item_id: int
    provider: str
    start_date: date
    end_date: date

def get_sample_data() -> tuple[List[Room], List[Item]]:
    rooms = [Room("Kitchen"), Room("Living Room")]
    items = [
        Item(name="Blender", room_id=1, purchase_date=date(2023, 5, 1), warranty_expiry=date(2026, 5, 1), tags=["small appliances"]),
        Item(name="Sofa", room_id=2, purchase_date=date(2022, 1, 15), notes="Needs cleaning"),
    ]
    return rooms, items
