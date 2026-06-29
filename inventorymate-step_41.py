# === Stage 41: Add plain text import for a simple line-based format ===
# Project: InventoryMate
import csv, json, os, sys
from pathlib import Path
def load_plain_text(path: str) -> list[dict]:
    items = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'): continue
                parts = [p.strip() for p in line.split('|')]
                if len(parts) < 3: continue
                items.append({
                    'id': parts[0],
                    'name': parts[1],
                    'room': parts[2] if len(parts) > 2 else '',
                    'warranty_months': int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else None,
                    'tags': [t.strip() for t in parts[4:]] if len(parts) > 4 else []
                })
    except FileNotFoundError:
        pass
    return items

def save_plain_text(items: list[dict], path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        for item in items:
            tags_str = '|'.join(item['tags']) if item['tags'] else ''
            warranty_str = str(item['warranty_months']) if item['warranty_months'] is not None else ''
            line = f"{item['id']}|{item['name']}|{item['room']}|{warranty_str}|{tags_str}"
            f.write(line + '\n')

def merge_plain_text(source_path: str, target_db: dict) -> int:
    new_items = load_plain_text(source_path)
    if not new_items: return 0
    for item in new_items:
        if item['id'] not in [i['id'] for i in target_db.values()]:
            target_db[item['id']] = item
    save_plain_text(list(target_db.values()), source_path)
    return len(new_items)
