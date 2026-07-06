# === Stage 53: Add command help text and usage examples ===
# Project: InventoryMate
def print_help():
    """Print usage examples and help text for InventoryMate commands."""
    print("InventoryMate Commands:")
    print("- list rooms: Show all registered rooms.")
    print("- add room <name>: Add a new room to the inventory.")
    print("- search items <query>: Search items by name, tag, or warranty status.")
    print("- export csv: Export current inventory to CSV file.")
    print("- export json: Export current inventory as JSON object.")
    print("- remove item <name>: Remove an item from its room's inventory.")
    print("For more info, visit https://github.com/InventoryMate")
