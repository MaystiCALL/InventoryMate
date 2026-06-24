# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: InventoryMate
SETTINGS_FILE = "inventory_settings.json"

def load_settings():
    try:
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "theme": "light",
            "default_room": "living room",
            "auto_backup": True,
            "backup_interval_days": 7,
            "export_format": "csv"
        }

def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)

def update_setting(key, value):
    settings = load_settings()
    if key in settings:
        settings[key] = value
        save_settings(settings)
        return True
    else:
        print(f"Setting '{key}' not found.")
        return False

def get_setting(key, default=None):
    try:
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            return settings.get(key, default)
    except FileNotFoundError:
        return default
