# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: InventoryMate
def update_item(item_id, new_data):
    """
    Updates an item in the inventory if it exists.
    Returns a tuple: (success: bool, message: str, updated_item: dict or None).
    Handles missing records gracefully without crashing.
    Assumes 'inventory' is a global dictionary or accessible scope.
    """
    if item_id not in inventory:
        return False, f"Item with ID '{item_id}' not found.", None

    existing = inventory[item_id]
    
    # Merge new_data into existing record, preserving missing keys from new_data
    for key, value in new_data.items():
        if value is not None:
            existing[key] = value

    # Optional: Validate specific fields if needed (e.g., warranty date format)
    # For now, we assume new_data contains valid values or None to clear.
    
    return True, f"Item '{item_id}' updated successfully.", existing
