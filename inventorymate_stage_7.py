# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: InventoryMate
def format_item(item):
    return f"[{item['room']}] {item['name']} ({item['category']}) - Warranty: {item.get('warranty', 'N/A')}"

def format_list(items, limit=10):
    if not items:
        print("No items found.")
        return
    for i in range(min(limit, len(items))):
        print(f"{i+1}. {format_item(items[i])}")
    if len(items) > limit:
        print(f"... and {len(items) - limit} more")

def format_detail(item):
    lines = [f"Item: {item['name']}", f"Room: {item['room']}", f"Category: {item['category']}"]
    if 'warranty' in item:
        lines.append(f"Warranty: until {item['warranty']}")
    if 'tags' in item and item['tags']:
        lines.append(f"Tags: {', '.join(item['tags'])}")
    print("\n".join(lines))
