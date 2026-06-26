# === Stage 35: Add active user switching and user-specific records ===
# Project: InventoryMate
from dataclasses import field, asdict
import json
from pathlib import Path

class User:
    def __init__(self, name):
        self.name = name
        self.records = []
    
    def to_dict(self):
        return {"name": self.name, "records": [asdict(r) for r in self.records]}
    
    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"])
        user.records = [InventoryItem(**r) for r in data.get("records", [])]
        return user

class InventoryItem:
    def __init__(self, name, room="General", warranty_days=0, tags=None):
        self.name = name
        self.room = room
        self.warranty_days = warranty_days
        self.tags = tags or []
    
    def is_warrantied(self):
        return self.warranty_days > 0 and not (self.created_at < get_current_timestamp() - timedelta(days=self.warranty_days))

def get_current_timestamp():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).timestamp()
