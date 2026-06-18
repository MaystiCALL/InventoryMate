# === Stage 20: Add duplicate detection for newly created records ===
# Project: InventoryMate
from typing import Optional, List
import hashlib
from datetime import date

def _get_record_hash(record: dict) -> str:
    content = f"{record.get('name', '')} {record.get('serial_number', '')} {record.get('category', '')}"
    return hashlib.md5(content.encode()).hexdigest()[:8]

class DuplicateDetector:
    def __init__(self, existing_records: List[dict]):
        self._hash_map = {}
        for rec in existing_records:
            h = _get_record_hash(rec)
            if h not in self._hash_map:
                self._hash_map[h] = []
            self._hash_map[h].append(rec)

    def check_new_record(self, new_record: dict) -> Optional[dict]:
        h = _get_record_hash(new_record)
        candidates = self._hash_map.get(h, [])
        if not candidates:
            return None
        best_match = max(candidates, key=lambda r: (len(r.get('name', '')) > 0 and len(r.get('serial_number', '')) > 0), default=None)
        if best_match is None or new_record['id'] == best_match['id']:
            return None
        return best_match

    def add_to_index(self, record: dict):
        h = _get_record_hash(record)
        if h not in self._hash_map:
            self._hash_map[h] = []
        self._hash_map[h].append(record)
