# === Stage 44: Add backup creation for the data file ===
# Project: InventoryMate
import json, os, datetime, uuid
from pathlib import Path

def backup_data(data_file: str) -> bool:
    if not os.path.exists(data_file):
        return False
    base = Path(data_file).parent
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = uuid.uuid4().hex[:8]
    backup_name = f"{Path(data_file).stem}_{timestamp}_{unique_id}.json"
    backup_path = base / "backups" / backup_name
    try:
        os.makedirs(str(base / "backups"), exist_ok=True)
        shutil.copy2(data_file, str(backup_path))
        return True
    except Exception:
        return False
