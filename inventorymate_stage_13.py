# === Stage 13: Add file save support using a configurable path ===
# Project: InventoryMate
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.data_dir = Path.home() / ".inventorymate"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = self.data_dir / "inventory.db"
        self.export_format = "csv"  # csv or json

def save_inventory(items: list[dict], config: Config):
    """Save inventory to CSV or JSON based on configuration."""
    path = Path(config.data_dir) / f"{config.export_format}"
    if config.export_format == "json":
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
    else:
        import csv
        if not items: return
        fieldnames = list(items[0].keys())
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(items)

def load_inventory(config: Config):
    """Load inventory from CSV or JSON based on configuration."""
    path = Path(config.data_dir) / f"{config.export_format}"
    if not path.exists(): return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if config.export_format == "json":
        import json
        return json.loads(content)
    else:
        import csv
        reader = csv.DictReader(f.splitlines())
        return list(reader)
