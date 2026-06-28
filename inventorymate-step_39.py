# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: InventoryMate
def repair_data_integrity(items):
    """Fix common data issues: missing rooms, invalid dates, duplicate IDs."""
    seen_ids = set()
    fixed_items = []
    
    for item in items:
        # Ensure room exists and is not empty string
        if not item.get('room'):
            item['room'] = 'Uncategorized'
        
        # Fix warranty date format YYYY-MM-DD or remove invalid dates
        try:
            if item.get('warranty_end') and len(item['warranty_end']) == 10:
                datetime.datetime.strptime(item['warranty_end'], '%Y-%m-%d')
        except ValueError:
            item.pop('warranty_end', None)
        
        # Handle duplicate IDs by appending a suffix if needed
        item_id = item.get('id') or item.get('_id')
        if not item_id:
            item['id'] = f"item_{len(fixed_items)}"
        elif item_id in seen_ids:
            base_name = str(item_id).split('_')[0] if '_' in str(item_id) else str(item_id)
            suffix = 1
            while True:
                candidate = f"{base_name}_{suffix}"
                if candidate not in seen_ids:
                    item['id'] = candidate
                    break
                suffix += 1
        
        seen_ids.add(item.get('id'))
        fixed_items.append(item)
    
    return fixed_items
