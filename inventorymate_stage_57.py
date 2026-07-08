# === Stage 57: Add structured result objects for command handlers ===
# Project: InventoryMate
class SearchResult:
    def __init__(self, id: str, name: str = "", room: str = "", tags: list[str] | None = None):
        self.id = id
        self.name = name
        self.room = room
        self.tags = tags or []

    def matches(self, query: str) -> bool:
        q = query.lower()
        return (q in self.name.lower() or q in self.room.lower()) and \
               any(q in t.lower() for t in self.tags) if self.tags else True


class ExportReport:
    def __init__(self, filename: str):
        self.filename = filename
        self.rows: list[dict] = []

    def append(self, item: dict[str, object]) -> None:
        row = {
            "id": getattr(item, "id", ""),
            "name": getattr(item, "name", ""),
            "room": getattr(item, "room", ""),
            "tags": ", ".join(getattr(item, "tags", [])),
        }
        self.rows.append(row)

    def write_csv(self) -> str:
        import csv, io
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["id", "name", "room", "tags"])
        for row in self.rows:
            w.writerow([row.get(k, "") for k in ["id", "name", "room", "tags"]])
        return buf.getvalue()

    def to_json(self) -> str:
        import json
        return json.dumps(self.rows, indent=2)
