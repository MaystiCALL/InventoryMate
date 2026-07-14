# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: InventoryMate
def merge_imports(existing_lines, new_block):
    """Merge imports from new_block into existing_lines, skipping obvious duplicates."""
    seen = {line.strip() for line in existing_lines if line.strip().startswith("import ")}
    merged = []
    skip_next = False
    for i, line in enumerate(new_block):
        stripped = line.strip()
        if not stripped.startswith("import ") and not skipped:
            continue
        skip_next = False
        if stripped in seen or stripped == "#":
            continue
        merged.append(line)

    return existing_lines[:len(existing_lines)] + merged
