# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: InventoryMate
class ItemPriority:
    def __init__(self, item):
        self.item = item

    def score(self):
        s = 0
        if self.item.warranty_expires and (self.item.warranty_expires - datetime.now()) < timedelta(days=90):
            s += 30
        elif not self.item.warranty:
            s -= 15
        tags = [t for t in self.item.tags if 'urgent' in t.lower() or 'important' in t.lower()]
        s += len(tags) * 20
        if self.item.last_inspected and (datetime.now() - self.item.last_inspected).days > 365:
            s += 10
        return s

    def recommend(self):
        items = [ItemPriority(i) for i in self.inventory.items]
        scored = sorted(items, key=lambda x: x.score(), reverse=True)
        top = scored[:5]
        recs = []
        for ip in top:
            if ip.item.warranty_expires and (ip.item.warranty_expires - datetime.now()) < timedelta(days=90):
                recs.append((ip.item.name, f"Warranty expires soon ({(ip.item.warranty_expires - datetime.now()).days} days)"))
            elif not ip.item.warranty:
                recs.append((ip.item.name, "No warranty found"))
            else:
                recs.append((ip.item.name, f"High priority item (score: {ip.score()})"))
        return recs

    @staticmethod
    def compute_inventory_score(items):
        total = sum(ItemPriority(i).score() for i in items)
        avg = total / len(items) if items else 0
        highest = max((ItemPriority(i).score() for i in items), default=0)
        return {"total": total, "average": round(avg, 1), "highest_priority_score": highest}
