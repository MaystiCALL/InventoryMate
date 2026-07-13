# === Stage 63: Add relationships between records where useful ===
# Project: InventoryMate
def setup_relationships(db):
    """Add cross-record relationships for richer queries."""
    # Room → Warranty: find warranties expiring soon per room
    warranty_expiry = db.execute(
        "SELECT item_id, w.expiration_date FROM warranties w "
        "JOIN items i ON w.item_id=i.id "
        "WHERE i.room_id IS NOT NULL AND w.expiration_date > :now "
        "ORDER BY w.expiration_date ASC",
        {"now": datetime.now()}
    ).fetchall()
    for wid, item_id, exp in warranty_expiry:
        db.execute(
            "INSERT OR IGNORE INTO relations (record1_type, record1_id, record2_type, record2_id, label) "
            "VALUES ('item', ?, 'warranty', ?, 'room_warranty')",
            [item_id, wid]
        )
    # Tag → Item: link tags to items via a reverse table
    db.execute(
        "CREATE TABLE IF NOT EXISTS tag_links (tag_id INTEGER, item_id INTEGER)"
    )
    for tname in db.execute("SELECT id FROM tags").fetchall():
        tid = tname[0]
        linked = db.execute(
            "SELECT DISTINCT i.id FROM items i JOIN item_tags it ON it.tag_id=i.id WHERE it.tag_id=?",
            [tid]
        ).fetchall()
        if not linked:
            continue
        ids = ", ".join(str(r[0]) for r in linked)
        db.execute(
            "INSERT OR REPLACE INTO tag_links (tag_id, item_id) VALUES (?, ?)",
            [tid, ids]  # SQLite allows multiple values via triggers; single row per pair
        )

setup_relationships(db)
