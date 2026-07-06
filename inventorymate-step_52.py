# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: InventoryMate
def _find_item_by_name(items, name):
    """Locate an item whose ``name`` matches exactly (case-insensitive)."""
    if not items:
        return None
    lower = name.lower()
    for it in items:
        if it["name"].lower() == lower:
            return it
    return None


def _filter_items(items, search=None):
    """Return a list of items matching ``search`` (None returns all)."""
    results = []
    for it in items:
        text = (it.get("notes") or "").lower()
        if search and search.lower() not in text:
            continue
        results.append(it)
    return results


def _export_items(items, fmt="csv"):
    """Export ``items`` to a CSV string. Returns the header row for empty lists."""
    if not items:
        return "name,warranty_expires,notes"
    lines = ["name,warranty_expires,notes"]
    for it in items:
        name = ",".join(it.get("name", "").split(",")).replace('"', '""')
        expires = (it.get("warranty_expires") or "").replace(",", ";").replace('"', '""')
        notes = (it.get("notes") or "").replace(",", ";").replace('"', '""')
        lines.append(f'"{name}",{expires},"{notes}"')
    return "\n".join(lines)


def _count_warranties(items):
    """Return a dict mapping warranty expiry dates to the count of items."""
    counts = {}
    for it in items:
        expires = (it.get("warranty_expires") or "").strip()
        if not expires:
            continue
        counts[expires] = counts.get(expires, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: kv[0]))


def _get_item_summary(items):
    """Return a summary string with total count and unique warranty dates."""
    if not items:
        return "No items found."
    return f"Total: {len(items)} item(s). Warranty expiries: {', '.join(_count_warranties(items))}."


def _validate_item(item):
    """Check that ``item`` has required fields; raise ValueError if missing."""
    for key in ("name", "warranty_expires"):
        if not item.get(key):
            raise ValueError(f"Item is missing required field: {key}")
