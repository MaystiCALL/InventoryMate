# === Stage 36: Add templates for quickly creating common records ===
# Project: InventoryMate
from datetime import date, timedelta
import random
from typing import Optional

class TemplateManager:
    def __init__(self):
        self.templates = {}

    def register(self, name: str, factory_func):
        self.templates[name] = factory_func

    def create_from_template(self, template_name: str, **kwargs) -> dict:
        if template_name not in self.templates:
            raise ValueError(f"Unknown template: {template_name}")
        factory = self.templates[template_name]
        return factory(**{**factory._defaults, **kwargs})

    def _generate_id(self):
        return f"{random.randint(1000, 9999)}-{date.today().strftime('%Y%m%d')}"

# Register common templates for quick inventory creation
TemplateManager.register("laptop", lambda: {
    "id": TemplateManager()._generate_id(),
    "name": "Laptop Model X",
    "category": "Electronics",
    "room": "Home Office",
    "purchase_date": date.today() - timedelta(days=random.randint(30, 365)),
    "warranty_expiry": (date.today() + timedelta(days=180)).strftime("%Y-%m-%d"),
    "tags": ["work", "portable"],
    "notes": "Primary work device."
})

TemplateManager.register("tv", lambda: {
    "id": TemplateManager()._generate_id(),
    "name": "Smart TV 55\"",
    "category": "Electronics",
    "room": "Living Room",
    "purchase_date": date.today() - timedelta(days=random.randint(90, 400)),
    "warranty_expiry": (date.today() + timedelta(days=365)).strftime("%Y-%m-%d"),
    "tags": ["entertainment"],
    "notes": "Main entertainment center."
})

TemplateManager.register("furniture", lambda: {
    "id": TemplateManager()._generate_id(),
    "name": "Wooden Chair",
    "category": "Furniture",
    "room": "Dining Room",
    "purchase_date": date.today() - timedelta(days=random.randint(100, 800)),
    "warranty_expiry": None,
    "tags": ["durable"],
    "notes": ""
})
