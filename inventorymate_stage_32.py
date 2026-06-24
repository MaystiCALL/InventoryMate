# === Stage 32: Add pagination helpers for long console output ===
# Project: InventoryMate
def paginate_items(items, page_size=10):
    total_pages = (len(items) + page_size - 1) // page_size if items else 0
    for p in range(1, total_pages + 1):
        start = (p - 1) * page_size
        end = start + page_size
        print(f"\n--- Page {p}/{total_pages} ---")
        for item in items[start:end]:
            print(item)

def filter_and_paginate(items, keyword=None, room=None, tag=None, page_size=10):
    filtered = []
    if keyword:
        kw_lower = keyword.lower()
        filtered = [i for i in items if any(kw_lower in str(v).lower() for v in i.values())]
    else:
        filtered = list(items)
    if room:
        filtered = [i for i in filtered if i.get('room') == room]
    if tag:
        filtered = [i for i in filtered if any(tag.lower() in str(v).lower() for v in i.values())]
    paginate_items(filtered, page_size)

def export_paginated(items, filename="inventory.txt", page_size=10):
    with open(filename, "w") as f:
        total_pages = (len(items) + page_size - 1) // page_size if items else 0
        for p in range(1, total_pages + 1):
            start = (p - 1) * page_size
            end = start + page_size
            f.write(f"\n--- Page {p}/{total_pages} ---\n")
            for item in items[start:end]:
                line = ", ".join(f"{k}: {v}" for k, v in sorted(item.items()))
                f.write(line + "\n")
