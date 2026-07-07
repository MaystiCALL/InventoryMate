# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: InventoryMate
def colorize(text, color):
    codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    reset = '\033[0m'
    code = codes.get(color, '')
    return f"{code}{text}{reset}" if code else text

def print_inventory_summary(inventory):
    rooms = inventory.get('rooms', [])
    tags = set()
    for item in inventory.get('items', []):
        tags.update(item.get('tags', []))
    print(f"{'─'*60}")
    print(colorize(f"InventoryMate – {len(rooms)} room(s), {len(tags)} tag(s)", 'cyan'))
    print(f"  Items: {len(inventory.get('items', []))}")
    if rooms:
        print(colorize("  Rooms:", 'green'))
        for r in rooms:
            print(f"    • {r['name']}")
    if tags:
        print(colorize("  Tags:", 'yellow'))
        for t in sorted(tags):
            print(f"    • {t}")
