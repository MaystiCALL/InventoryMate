# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: InventoryMate
def bulk_delete(items, confirm_flag=False):
    if items is None:
        return []
    if not isinstance(items, list):
        items = [items]
    deleted = []
    for item in items:
        if item.get('deleted') and confirm_flag:
            continue
        if confirm_flag or 'deleted' not in item:
            item['deleted'] = True
            deleted.append(item)
    return deleted
