# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: InventoryMate
import unittest
from inventorymate.helpers import validate_item, create_tag, normalize_name

class TestHelpers(unittest.TestCase):
    def test_validate_item_valid(self):
        self.assertTrue(validate_item("Laptop", "2023", 5))
    
    def test_validate_item_invalid_date(self):
        with self.assertRaises(ValueError):
            validate_item("Phone", "1900-01-01", 1)
    
    def test_create_tag_valid(self):
        tag = create_tag("electronics")
        self.assertEqual(tag, {"name": "Electronics", "color": "#3498db"})
    
    def test_normalize_name_case_insensitive(self):
        self.assertEqual(normalize_name("LAPTOP"), normalize_name("laptop"))

if __name__ == "__main__":
    unittest.main()
