# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: InventoryMate
from datetime import datetime, timedelta
import json
from pathlib import Path

def archive_old_records(db_path: str, days_threshold: int = 365):
    """Move records older than threshold to an 'archive' directory."""
    db_file = Path(db_path)
    if not db_file.exists(): return
    
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    archive_dir = Path(db_file.parent, "archive")
    
    with open(db_file, "r", encoding="utf-8") as f:
        records = json.load(f)
    
    active_records = []
    archived_items = []
    
    for item in records:
        if item.get("completed_at"):
            completed_date = datetime.fromisoformat(item["completed_at"].replace("Z", "+00:00"))
            if completed_date < cutoff_date:
                archived_items.append(item)
            else:
                active_records.append(item)
        else:
            active_records.append(item)
    
    if not archived_items: return
    
    archive_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = Path(archive_dir, f"inventory_{timestamp}.json")
    
    with open(archive_file, "w", encoding="utf-8") as f:
        json.dump(archived_items, f, indent=2, ensure_ascii=False)

def restore_from_archive(db_path: str):
    """Restore the most recent archive back to the main database."""
    db_file = Path(db_path)
    if not db_file.exists(): return
    
    archive_dir = Path(db_file.parent, "archive")
    if not archive_dir.exists() or not list(archive_dir.glob("*.json")): return
    
    latest_archive = max(list(archive_dir.glob("*.json")), key=lambda p: p.stat().st_mtime)
    
    with open(latest_archive, "r", encoding="utf-8") as f:
        archived_data = json.load(f)
    
    with open(db_file, "w", encoding="utf-8") as f:
        current_records = json.load(f) if db_file.exists() else []
        # Merge or replace logic depending on desired behavior; here we append to existing active records
        for item in archived_data:
            if not any(r.get("id") == item.get("id") and r.get("completed_at", "") != item.get("completed_at", "") 
                       for r in current_records):
                current_records.append(item)
        
        json.dump(current_records, f, indent=2, ensure_ascii=False)
