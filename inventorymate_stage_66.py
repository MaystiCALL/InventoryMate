# === Stage 66: Add export of a short status dashboard ===
# Project: InventoryMate
def export_dashboard(inventory):
    """Export a compact status dashboard."""
    total_items = sum(1 for r in inventory['rooms'] for item in r.get('items', []))
    low_stock = sum(1 for room in inventory['rooms']
                    for item in room.get('items', []) if item.get('quantity', 0) <= 5)
    warranty_count = sum(1 for item in [item for room in inventory['rooms'] for item in room.get('items', [])]
                         if item.get('warranty_remaining', '') and 'expired' not in str(item.get('warranty_remaining', '')))
    tags_used = set()
    for room in inventory['rooms']:
        for item in room.get('items', []):
            tags_used.update(item.get('tags', []))
    return {'total_items': total_items, 'low_stock': low_stock, 'active_tags': len(tags_used), 'warranty_active': warranty_count}
