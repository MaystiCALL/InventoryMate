# === Stage 34: Add support for multiple local user profiles ===
# Project: InventoryMate
import json, os
from pathlib import Path

class ProfileManager:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir) / "profiles"
        self.profiles_file = self.data_dir / "active_profile.json"
        self._ensure_dirs()

    def _ensure_dirs(self):
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True, exist_ok=True)

    def load_profiles(self):
        profiles = {}
        for f in self.data_dir.glob("*.json"):
            try:
                with open(f) as fp:
                    data = json.load(fp)
                    if "name" in data and "inventory_data" in data:
                        profiles[data["name"]] = {"path": str(f), **data}
            except (json.JSONDecodeError, IOError):
                continue
        return profiles

    def get_active_profile(self):
        try:
            with open(self.profiles_file) as fp:
                return json.load(fp)["name"]
        except (FileNotFoundError, KeyError):
            return None

    def set_active_profile(self, name):
        if not self.get_profiles().get(name):
            raise ValueError(f"Profile '{name}' not found")
        with open(self.profiles_file, "w") as fp:
            json.dump({"name": name}, fp)

    def get_profiles(self):
        return self.load_profiles()
