# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: InventoryMate
def seed_demo_data(db):
    """Populate the database with deterministic sample data for demo/development."""
    from datetime import date, timedelta
    from uuid import uuid4
    rooms = ["Kitchen", "Living Room", "Bedroom", "Office", "Garage"]
    tags = ["Electronics", "Furniture", "Books", "Kitchenware", "Tools", "Decor", "Sports", "Clothing"]
    for i, room in enumerate(rooms):
        db.rooms.insert_one({"name": room, "description": f"The {room} area.", "created_at": date.today() - timedelta(days=i)})
    for t in tags:
        db.tags.insert_one({"name": t})
    items = [
        {"name": "Smartphone", "room_id": str(uuid4()), "tags": ["Electronics"], "purchased_on": date(2023, 1, 15), "warranty_start": date(2023, 1, 16), "warranty_end": date(2026, 1, 15)},
        {"name": "Laptop", "room_id": str(uuid4()), "tags": ["Electronics"], "purchased_on": date(2022, 6, 1), "warranty_start": date(2022, 6, 2), "warranty_end": date(2025, 6, 1)},
        {"name": "Coffee Machine", "room_id": str(uuid4()), "tags": ["Kitchenware"], "purchased_on": date(2023, 3, 10), "warranty_start": date(2023, 3, 11), "warranty_end": date(2026, 3, 10)},
        {"name": "Wooden Chair", "room_id": str(uuid4()), "tags": ["Furniture"], "purchased_on": date(2021, 9, 5), "warranty_start": None, "warranty_end": None},
        {"name": "Python Cookbook", "room_id": str(uuid4()), "tags": ["Books"], "purchased_on": date(2023, 7, 20), "warranty_start": None, "warranty_end": None},
    ]
    for item in items:
        db.items.insert_one(item)
