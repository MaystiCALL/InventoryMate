# === Stage 38: Add data integrity checks for broken references ===
# Project: InventoryMate
class IntegrityChecker:
    def __init__(self, db):
        self.db = db
    
    def check_broken_room_refs(self):
        broken_items = []
        for item in self.db['items']:
            if item.get('room_id') and not any(i['id'] == item['room_id'] for i in self.db['rooms']):
                broken_items.append(item)
        return broken_items
    
    def check_broken_tag_refs(self):
        broken_items = []
        for item in self.db['items']:
            if isinstance(item.get('tags'), list):
                for tag_id in item['tags']:
                    if not any(t['id'] == tag_id for t in self.db['tags']):
                        broken_items.append({'item': item, 'broken_tag': tag_id})
        return broken_items
    
    def check_broken_warranty_refs(self):
        broken_items = []
        for item in self.db['items']:
            if item.get('warranty_id') and not any(w['id'] == item['warranty_id'] for w in self.db['warranties']):
                broken_items.append(item)
        return broken_items
    
    def fix_broken_refs(self, action='remove'):
        items_to_remove = []
        if action == 'remove':
            for b in self.check_broken_room_refs():
                items_to_remove.append(b['id'])
            for b in self.check_broken_tag_refs():
                if b['item']['id'] not in items_to_remove:
                    items_to_remove.append(b['item']['id'])
        elif action == 'clear_tags':
            for b in self.check_broken_tag_refs():
                b['item']['tags'].remove(b['broken_tag'])
        return items_to_remove
