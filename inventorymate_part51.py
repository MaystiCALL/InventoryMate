# === Stage 51: Add unit tests for search and filter behavior ===
# Project: InventoryMate
from unittest.mock import patch, MagicMock
import pytest
from inventory_mate.core.search_engine import SearchEngine

@pytest.fixture
def search_engine():
    return SearchEngine()

@patch('inventory_mate.db.database.get_all_items')
def test_search_by_name(mock_get_items, search_engine):
    mock_get_items.return_value = [
        {'name': 'Laptop', 'room': 'Bedroom'},
        {'name': 'Phone', 'room': 'Kitchen'}
    ]
    results = search_engine.search('Laptop')
    assert len(results) == 1
    assert results[0]['name'] == 'Laptop'

@patch('inventory_mate.db.database.get_all_items')
def test_filter_by_room(mock_get_items, search_engine):
    mock_get_items.return_value = [
        {'name': 'TV', 'room': 'Living Room'},
        {'name': 'Console', 'room': 'Living Room'}
    ]
    results = search_engine.filter('Living Room')
    assert len(results) == 2

@patch('inventory_mate.db.database.get_all_items')
def test_combined_search_and_filter(mock_get_items, search_engine):
    mock_get_items.return_value = [
        {'name': 'Laptop', 'room': 'Bedroom'},
        {'name': 'Phone', 'room': 'Kitchen'}
    ]
    results = search_engine.search('Phone').filter('Kitchen')
    assert len(results) == 1
