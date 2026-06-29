# === Stage 40: Add plain text report export ===
# Project: InventoryMate
def export_to_text(items, rooms=None):
    if not items: return ""
    buffer = []
    for room in sorted(rooms.values(), key=lambda r: r['name']) if rooms else [None]:
        if room is None or (room and item.get('roomId') == room['id']):
            continue
        for item in items:
            if room and item.get('roomId') != room['id']:
                continue
            buffer.append(f"{item['name']} | {item['quantity']}x | Warranty: {item.get('warranty', 'None')}")
    return "\n".join(buffer)
