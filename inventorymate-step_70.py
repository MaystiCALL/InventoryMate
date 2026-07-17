# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: InventoryMate
import json, os, sys
from datetime import datetime

def clear_inventory():
    """Clear all inventory data with confirmation."""
    if not os.path.exists("inventory.json"):
        print("No inventory found to clear.")
        return
    
    confirm = input("\nThis will delete ALL items. Type 'yes' to confirm: ").strip().lower()
    
    if confirm != "yes":
        print("Operation cancelled.")
        return
    
    try:
        with open("inventory.json", "r") as f:
            data = json.load(f)
        
        rooms = []
        items = []
        tags = []
        
        for room in data.get("rooms", []):
            if room["items"]:
                print(f"Room '{room['name']}' has {len(room['items'])} item(s). Clearing...")
                room["items"] = []
            rooms.append(room)
        
        items.clear()
        tags.clear()
        
        data["rooms"] = rooms
        data["items"] = items
        data["tags"] = tags
        data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        with open("inventory.json", "w") as f:
            json.dump(data, f, indent=2)
        
        print("Inventory cleared successfully.")
    
    except Exception as e:
        print(f"Error clearing inventory: {e}")

if __name__ == "__main__":
    clear_inventory()
