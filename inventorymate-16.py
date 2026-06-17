# === Stage 16: Add argparse support for the most common commands ===
# Project: InventoryMate
import argparse, json, os, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(prog="InventoryMate", description="Home inventory manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List items
    list_parser = subparsers.add_parser("list", help="List all items")
    list_parser.add_argument("--room", type=str, default=None, help="Filter by room name")
    list_parser.add_argument("--tags", "-t", nargs="+", default=[], help="Filter by tags")
    
    # Add item
    add_parser = subparsers.add_parser("add", help="Add a new item")
    add_parser.add_argument("-n", "--name", required=True, help="Item name")
    add_parser.add_argument("-r", "--room", default=None, help="Room (kitchen, bedroom)")
    add_parser.add_argument("-w", "--warranty", type=int, default=0, help="Warranty months")
    add_parser.add_argument("-t", "--tags", nargs="+", default=[], help="Tags")
    
    # Export data
    export_parser = subparsers.add_parser("export", help="Export inventory to JSON")
    export_parser.add_argument("--file", "-f", type=str, required=True, help="Output file path")
    
    args = parser.parse_args()
    
    if not os.path.exists("inventory.json"):
        print("[Error] No inventory data found. Run 'add' first.")
        sys.exit(1)
    
    with open("inventory.json", "r", encoding="utf-8") as f:
        items = json.load(f)
    
    if args.command == "list":
        filtered = items
        if args.room:
            filtered = [i for i in filtered if i.get("room") == args.room]
        if args.tags:
            filtered = [i for i in filtered if any(t in i.get("tags", []) for t in args.tags)]
        print(json.dumps(filtered, indent=2))
    
    elif args.command == "add":
        new_item = {
            "name": args.name,
            "room": args.room or "",
            "warranty_months": args.warranty,
            "tags": list(args.tags) if args.tags else []
        }
        items.append(new_item)
        with open("inventory.json", "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)
        print(f"[OK] Added '{args.name}' to inventory.")
    
    elif args.command == "export":
        Path(args.file).write_text(json.dumps(items, indent=2))
        print(f"[OK] Exported {len(items)} items to '{args.file}'.")

if __name__ == "__main__":
    main()
