# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: InventoryMate
def generate_changelog(entries, max_lines=20):
    """Generate a compact changelog from activity log entries."""
    lines = []
    for entry in entries:
        if len(lines) >= max_lines:
            break
        date = entry.get("date", "unknown")
        change_type = entry.get("type", "change")
        description = entry.get("description", "")
        if not description.strip():
            continue
        line = f"- **{date}**: {description}"
        lines.append(line)
    return "\n".join(lines)
