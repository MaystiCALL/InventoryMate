# === Stage 43: Add CSV import for the primary record type ===
# Project: InventoryMate
import csv, io

def import_csv(file_path):
    items = []
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get('name'): continue
                item = {
                    'id': int(row['id']) if row.get('id') else len(items)+1,
                    'name': row['name'],
                    'room': row.get('room', ''),
                    'brand': row.get('brand', ''),
                    'model': row.get('model', ''),
                    'purchase_date': row.get('purchase_date', ''),
                    'warranty_end': row.get('warranty_end', ''),
                    'tags': [t.strip() for t in row.get('tags', '').split(';') if t.strip()],
                }
                items.append(item)
    except FileNotFoundError:
        pass
    return items
