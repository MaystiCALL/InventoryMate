# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: InventoryMate
def _tag_summary(items, tag):
    return [i for i in items if tag in i.get('tags', [])]

def add_tag(item_id, tag_name):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item and 'tags' not in item:
        item['tags'] = []
    if isinstance(item['tags'], list) and tag_name not in item['tags']:
        item['tags'].append(tag_name)

def remove_tag(item_id, tag_name):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item and 'tags' in item:
        if isinstance(item['tags'], list):
            item['tags'] = [t for t in item['tags'] if t != tag_name]

def get_tagged_items(tag_name):
    return _tag_summary(inventory, tag_name)
