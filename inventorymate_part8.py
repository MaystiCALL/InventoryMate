# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: InventoryMate
class InventoryFilter:
    def __init__(self, items):
        self.items = items
    
    def filter_by_status(self, status=None):
        if status is None: return self.items
        return [i for i in self.items if i.get('status') == status]
    
    def filter_by_category(self, category=None):
        if category is None: return self.items
        return [i for i in self.items if i.get('category') == category]
    
    def filter_by_owner(self, owner=None):
        if owner is None: return self.items
        return [i for i in self.items if i.get('owner') == owner]
    
    def filter_by_tag(self, tag=None):
        if tag is None: return self.items
        return [i for i in self.items if tag in i.get('tags', [])]
    
    def apply_all_filters(self, status=None, category=None, owner=None, tag=None):
        result = self.items
        if status: result = self.filter_by_status(status)
        if category: result = self.filter_by_category(category)
        if owner: result = self.filter_by_owner(owner)
        if tag: result = self.filter_by_tag(tag)
        return result
