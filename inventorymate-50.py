# === Stage 50: Add unit tests for import and export behavior ===
# Project: InventoryMate
import json, os, tempfile
from pathlib import Path
from inventorymate.models import Item, Room, Tag, Warranty
from inventorymate.services.inventory_service import InventoryService

def test_import_export_roundtrip():
    with tempfile.TemporaryDirectory() as tmpdir:
        service = InventoryService(Path(tmpdir))
        
        # Create sample data
        room = Room(name="Living Room")
        tag = Tag(name="Electronics", color="#FF5733")
        warranty = Warranty(brand="Samsung", start_date="2023-01-01", end_date="2026-01-01")
        item = Item(name="TV", room=room, tags=[tag], warranty=warranty)
        
        service.add_item(item)
        
        # Export to JSON
        json_path = Path(tmpdir) / "inventory.json"
        service.export_to_json(json_path)
        
        assert json_path.exists()
        with open(json_path) as f:
            data = json.load(f)
            
        assert len(data["items"]) == 1
        assert data["items"][0]["name"] == "TV"
        assert data["items"][0]["room"]["name"] == "Living Room"
        
        # Import back and verify
        service2 = InventoryService(Path(tmpdir))
        service2.import_from_json(json_path)
        
        items_count = len(service2.get_all_items())
        assert items_count == 1
        
        imported_item = service2.get_item_by_name("TV")
        assert imported_item is not None
        assert imported_item.warranty.end_date == "2026-01-01"
