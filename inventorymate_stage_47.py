# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: InventoryMate
from inventory import Inventory, Item, Room, Warranty, Tag

def run_demo():
    inv = Inventory()
    
    # Setup rooms and tags
    living_room = Room("Living Room")
    kitchen = Room("Kitchen")
    electronics_tag = Tag("Electronics")
    fragile_tag = Tag("Fragile")
    
    # Create items with warranties
    tv = Item("Smart TV", "Sony", 2023, 150.0)
    tv.add_room(living_room)
    tv.add_tag(electronics_tag)
    tv.set_warranty(Warranty(24, "years"))
    
    blender = Item("Blender", "Vitamix", 2022, 300.0)
    blender.add_room(kitchen)
    blender.add_tag(fragile_tag)
    blender.set_warranty(Warranty(5, "years"))
    
    # Add items to inventory
    inv.add_item(tv)
    inv.add_item(blender)
    
    # Search and filter
    search_result = inv.search("Sony")
    print(f"Found {len(search_result)} Sony items.")
    
    # Export report
    report = inv.export_report()
    print(report[:100])

if __name__ == "__main__":
    run_demo()
