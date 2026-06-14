# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: InventoryMate
class SearchEngine:
    def __init__(self, items):
        self._items = list(items)
        self._index = {k.lower(): [] for k in ('name', 'room', 'tag', 'description')}
        for item in self._items:
            key_map = {'name': 'name', 'room': 'room', 'tag': 'tags'}
            if hasattr(item, 'get'): d = item.get(key_map[k], '')
            else: d = getattr(item, k, [])
            if isinstance(d, str): self._index[k.lower()].append((d.lower(), id(item)))
            elif isinstance(d, list):
                for t in d: self._index[k.lower()].append((t.lower(), id(item)))

    def search(self, query):
        q = query.strip().lower() if query else ''
        if not q: return [i for i in self._items]
        hits = set()
        for field, pairs in self._index.items():
            for _, item_id in pairs:
                if q in pairs[0]: hits.add(item_id)
        # Fallback to full scan if no index match found (e.g. complex queries)
        return [self._items[i] for i in range(len(self._items)) if any(q in str(getattr(i, k, '')).lower() for k in ('name', 'room', 'tag')) or q in getattr(i, 'description', '').lower()]
