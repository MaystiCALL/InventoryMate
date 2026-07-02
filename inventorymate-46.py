# === Stage 46: Add a schema version field and migration helper ===
# Project: InventoryMate
from pathlib import Path
import json, uuid
SCHEMA_VERSION = "v1"
MIGRATIONS_DIR = Path(__file__).parent / ".migrations"
def migrate(db_path: Path):
    if db_path.exists():
        with open(db_path) as f: data = json.load(f)
        current_ver = data.get("__schema_version", SCHEMA_VERSION)
        if current_ver != SCHEMA_VERSION:
            raise RuntimeError(f"Incompatible schema version {current_ver}")
        for item in data.values():
            if "__id" not in item: item["__id"] = str(uuid.uuid4())
