# === Stage 37: Add recommendations for the next useful action ===
# Project: InventoryMate
from typing import List, Optional
import json
from datetime import date, timedelta
from pathlib import Path

def get_next_action_suggestions(inventory: dict) -> List[str]:
    """Generate actionable recommendations based on inventory state."""
    suggestions = []
    
    # Check for items expiring soon (warranty < 30 days or maintenance due)
    today = date.today()
    for room, items in inventory.items():
        if not isinstance(items, list): continue
        for item in items:
            warranty_end = None
            maint_due = None
            
            # Parse warranty end date if exists
            if "warranty" in item and isinstance(item["warranty"], dict) and "end_date" in item["warranty"]:
                try:
                    warranty_end = datetime.strptime(item["warranty"]["end_date"], "%Y-%m-%d").date()
                except ValueError: pass
            
            # Parse maintenance due date if exists
            if "maintenance" in item and isinstance(item["maintenance"], dict) and "due_date" in item["maintenance"]:
                try:
                    maint_due = datetime.strptime(item["maintenance"]["due_date"], "%Y-%m-%d").date()
                except ValueError: pass
            
            # Add suggestion for expiring warranty
            if warranty_end and today <= warranty_end < (today + timedelta(days=30)):
                suggestions.append(f"⚠️ Warranty ending soon for '{item.get('name', 'Unknown')}' in {room}.")
            
            # Add suggestion for upcoming maintenance
            if maint_due and today <= maint_due < (today + timedelta(days=60)):
                suggestions.append(f"🔧 Maintenance due for '{item.get('name', 'Unknown')}' in {room} on {maint_due.strftime('%Y-%m-%d')}")

    # Check for items without tags or descriptions to improve searchability
    for room, items in inventory.items():
        if not isinstance(items, list): continue
        for item in items:
            missing_data = []
            if not item.get("description"): missing_data.append("description")
            if not item.get("tags"): missing_data.append("tags")
            
            if missing_data:
                suggestions.append(f"📝 Add {', '.join(missing_data)} to '{item.get('name', 'Unknown')}' in {room}.")

    # Check for duplicate names across rooms (simple check)
    name_counts = {}
    for room, items in inventory.items():
        if not isinstance(items, list): continue
        for item in items:
            name = item.get("name", "").lower()
            if name:
                name_counts[name] = name_counts.get(name, 0) + 1
    
    duplicates = [name for name, count in name_counts.items() if count > 1]
    if duplicates:
        suggestions.append(f"🔄 Consider renaming items with duplicate names: {', '.join(duplicates)}.")

    return suggestions
