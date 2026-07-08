# === Stage 56: Add compact error classes for domain failures ===
# Project: InventoryMate
class InventoryError(Exception):
    """Base class for all inventory domain errors."""


class RoomNotFoundError(InventoryError):
    pass


class WarrantyExpiredError(InventoryError):
    pass


class TagConflictError(InventoryError):
    pass


class SearchSyntaxError(InventoryError):
    pass


class ExportFormatError(InventoryError):
    pass
