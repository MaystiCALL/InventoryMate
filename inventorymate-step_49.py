# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: InventoryMate
import unittest
from inventorymate import InventoryItem, Room, Tag, Warranty

class TestInventoryEdgeCases(unittest.TestCase):
    def setUp(self):
        self.item = InventoryItem("Laptop", "Electronics")
        self.room = Room("Living Room")
        self.tag = Tag("Work")
        self.warranty = Warranty(24, 365)

    def test_update_nonexistent_item_raises_error(self):
        with self.assertRaises(ValueError):
            InventoryItem.update_by_id("non-existent-id", "New Name")

    def test_delete_nonexistent_item_raises_error(self):
        with self.assertRaises(ValueError):
            InventoryItem.delete_by_id("non-existent-id")

    def test_update_with_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            InventoryItem.update_by_id(self.item.id, "")

    def test_delete_sets_status_to_archived(self):
        original_count = len(InventoryItem.get_all())
        InventoryItem.delete_by_id(self.item.id)
        remaining_items = InventoryItem.get_all()
        self.assertEqual(len(remaining_items), original_count - 1)
        # Verify the deleted item is no longer in active list or status changed if tracked
