# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: InventoryMate
class CommandDispatcher:
    def __init__(self, inventory):
        self.inventory = inventory
        self.commands = {
            'add': self._cmd_add,
            'list': self._cmd_list,
            'search': self._cmd_search,
            'export': self._cmd_export,
            'help': self._cmd_help,
        }

    def dispatch(self, text):
        parts = text.strip().lower().split(maxsplit=1)
        if not parts: return "No command."
        cmd_name = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        handler = self.commands.get(cmd_name)
        if handler is None: return f"Unknown command: {cmd_name}"
        try:
            result = handler(args)
            return str(result)
        except Exception as e:
            return f"Error executing '{cmd_name}': {e}"

    def _cmd_add(self, args):
        if not args: return "Usage: add <room> <item>"
        room, item = (args.split(maxsplit=1) + [None])[:2]
        if not room or not item: return "Invalid arguments for 'add'."
        self.inventory.add_item(room, item)
        return f"Added '{item}' to room '{room}'."

    def _cmd_list(self, args):
        rooms = list(self.inventory.rooms.keys())
        if not rooms: return "No items found."
        lines = [f"{r}: {', '.join(sorted(self.inventory.rooms[r]))}" for r in sorted(rooms)]
        return "\n".join(lines)

    def _cmd_search(self, args):
        query = args.lower() if args else ""
        matches = []
        for room, items in self.inventory.rooms.items():
            for item in items:
                if query and query not in (room + " " + item).lower(): continue
                matches.append(f"{room}: {item}")
        return "\n".join(matches) if matches else "No matching items."

    def _cmd_export(self, args):
        fmt = args or "csv"
        try:
            self.inventory.export(fmt)
            return f"Exported to '{fmt}' format successfully."
        except Exception as e:
            return f"Export failed: {e}"

    def _cmd_help(self, args):
        cmds = "\n".join([f"{k}: {v.__name__}()" for k, v in self.commands.items()])
        return "Available commands:\n" + cmds
