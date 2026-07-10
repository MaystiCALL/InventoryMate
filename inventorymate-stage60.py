# === Stage 60: Add saved views for frequently used filters ===
# Project: InventoryMate
class SavedView:
    """Preserve a filter configuration for quick re-application."""

    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    def apply(self, inventory):
        """Re-apply saved view to current inventory."""
        if self.filters:
            return self._apply_filters(inventory)
        return inventory

    def _apply_filters(self, inventory):
        for key, value in self.filters.items():
            if hasattr(inventory, key):
                setattr(inventory, key, value)
        return inventory

    @staticmethod
    def from_dict(data):
        """Create a SavedView from a dictionary representation."""
        return SavedView(
            name=data.get("name", "Unnamed View"),
            filters=data.get("filters", {}),
        )

    def to_dict(self):
        """Convert saved view to a dictionary for serialization."""
        return {
            "name": self.name,
            "filters": self.filters,
        }

    def __repr__(self):
        return f"SavedView(name={self.name!r}, filters={len(self.filters)})"
