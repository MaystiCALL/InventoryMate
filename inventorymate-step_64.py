# === Stage 64: Add validation for relationship references ===
# Project: InventoryMate
from datetime import date


def validate_references(records):
    """Validate that foreign-key references in records are consistent."""
    errors = []
    for record in records:
        if "room_id" in record and record["room_id"] is not None:
            room_ids = {r["id"] for r in record.get("_rooms", []) or []}
            if record["room_id"] not in room_ids:
                errors.append(f"{record.get('name', 'Item')} (id={record['id']}) references unknown room")

        if "warranty_end" in record and isinstance(record["warranty_end"], date):
            if record["warranty_start"] is not None and record["warranty_end"] < record["warranty_start"]:
                errors.append(f"{record.get('name', 'Item')} (id={record['id']}) has warranty end before start")

        if "tags" in record and isinstance(record["tags"], list):
            for tag in record["tags"]:
                if isinstance(tag, dict) and tag.get("id") is not None:
                    tag_ids = {t["id"] for t in record.get("_tags", []) or []}
                    if tag["id"] not in tag_ids:
                        errors.append(f"{record.get('name', 'Item')} (id={record['id']}) references unknown tag id")

    return errors
