# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: InventoryMate
class InventorySorter:
    def __init__(self, items):
        self.items = list(items)

    def sort_by_title(self, reverse=False):
        return sorted(self.items, key=lambda x: (x.get('title', '').lower(), x.get('id', 0)), reverse=reverse)

    def sort_by_date(self, field='purchase_date', reverse=True):
        return sorted(self.items, key=lambda x: x.get(field, ''), reverse=reverse)

    def sort_by_priority(self, priority_map=None, reverse=False):
        if not priority_map:
            priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        return sorted(self.items, key=lambda x: priority_map.get(x.get('priority', 'low'), 99), reverse=reverse)

    def sort_by_last_update(self, field='last_updated_at', reverse=True):
        return sorted(self.items, key=lambda x: x.get(field, ''), reverse=reverse)
