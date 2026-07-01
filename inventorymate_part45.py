# === Stage 45: Add restore from backup with validation ===
# Project: InventoryMate
import json, os, hashlib, datetime
from pathlib import Path

def validate_and_restore(backup_path: str, target_dir: str) -> bool:
    if not backup_path.endswith('.json'): return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        required_keys = {'rooms', 'items', 'tags'}
        if not all(k in data for k in required_keys): raise ValueError("Invalid schema")
        os.makedirs(target_dir, exist_ok=True)
        backup_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:8]
        restore_path = Path(target_dir) / f"inventory_{backup_hash}.json"
        with open(restore_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[RESTORE] Validated and restored from {backup_path} to {restore_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Restore failed: {e}")
        return False
