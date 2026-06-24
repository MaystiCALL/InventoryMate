# === Stage 31: Add compact table rendering for long lists ===
# Project: InventoryMate
def render_compact_table(items, columns):
    if not items: return ""
    widths = [max(len(str(item.get(col, ''))) for item in items) + 2 for col in columns]
    header = " | ".join(f"{col[:w]}{c}" for c, w in zip(columns, widths))
    separator = "-+-".join("-" * (w + 2) for w in widths)
    rows = []
    for item in items:
        row_parts = [str(item.get(col, ''))[:w] if col else "" for col, w in zip(columns, widths)]
        rows.append(" | ".join(row_parts))
    return "\n".join([header, separator] + rows)
