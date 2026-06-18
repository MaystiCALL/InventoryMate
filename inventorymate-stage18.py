# === Stage 18: Add an activity log with timestamps and action names ===
# Project: InventoryMate
from datetime import datetime, timezone
import logging
from typing import Optional

class ActivityLogger:
    def __init__(self):
        self._log_file = "inventory_mate.log"
        self._setup_logger()

    def _setup_logger(self):
        handler = logging.FileHandler(self._log_file)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - [%(action_name)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        self.logger = logging.getLogger("InventoryMate")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def log_action(self, action_name: str, message: Optional[str] = None):
        timestamp = datetime.now(timezone.utc).isoformat()
        full_message = f"{message}" if message else ""
        log_entry = f"[{timestamp}] {action_name}: {full_message}"
        self.logger.info(log_entry)

    def record_item_add(self, item_id: str):
        self.log_action("ITEM_ADDED", f"Added new item with ID: {item_id}")

    def record_item_delete(self, item_id: str):
        self.log_action("ITEM_DELETED", f"Removed item with ID: {item_id}")

    def record_room_create(self, room_name: str):
        self.log_action("ROOM_CREATED", f"Created new room: {room_name}")

    def record_search_performed(self, query: str):
        self.log_action("SEARCH_PERFORMED", f"Searched for items matching query: '{query}'")

    def export_report(self, filename: str):
        self.log_action("EXPORT_GENERATED", f"Exported report to file: {filename}")
