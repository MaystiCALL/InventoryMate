# === Stage 22: Add favorite records and quick favorite listing ===
# Project: InventoryMate
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._ensure_table()

    def _ensure_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
        self.db.commit()

    def add_favorite(self, item_id: int) -> bool:
        try:
            self.cursor.execute("INSERT INTO favorites (item_id) VALUES (?)", (item_id,))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_favorite(self, item_id: int):
        self.cursor.execute("DELETE FROM favorites WHERE item_id = ?", (item_id,))
        self.db.commit()

    def is_favorited(self, item_id: int) -> bool:
        cursor = self.cursor.execute(
            "SELECT 1 FROM favorites WHERE item_id = ? LIMIT 1", (item_id,)
        )
        return cursor.fetchone() is not None

    def get_favorite_items(self):
        cursor = self.cursor.execute("""
            SELECT f.id, i.name, i.room, i.tags, f.created_at
            FROM favorites f
            JOIN items i ON f.item_id = i.id
            ORDER BY f.created_at DESC
        """)
        return cursor.fetchall()

    def close(self):
        self.db.close()
