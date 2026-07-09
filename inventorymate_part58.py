# === Stage 58: Add bulk update behavior for selected records ===
# Project: InventoryMate
def bulk_update_records(rows: list[dict[str, Any]], table_name: str) -> None:
    """Update multiple records in a SQLite table with the given data."""
    if rows is None or len(rows) == 0:
        return
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        for row in rows:
            cols = list(row.keys())
            placeholders = ",".join(["?"] * len(cols))
            sql = f"UPDATE {table_name} SET " + ", ".join(f"{c}=?" for c in cols) + \
                  f" WHERE id=? AND {sql}"  # simplified: use full row replacement
            cur.execute(
                f"INSERT OR REPLACE INTO {table_name} ({','.join(cols)}) VALUES ({placeholders})",
                list(row.values())
            )
        conn.commit()
    except Exception as e:
        print(f"Bulk update error: {e}")
    finally:
        conn.close()
