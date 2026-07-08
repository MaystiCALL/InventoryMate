# === Stage 55: Add a setting to disable colorized output ===
# Project: InventoryMate
import os

def colorize(text, color):
    """Return ANSI-colored text."""
    return f"\033[{color}m{text}\033[0m"

def is_color_enabled():
    """Check whether the terminal supports colors (no FORCE_NO_COLOR env)."""
    if os.environ.get("FORCE_NO_COLOR", "").lower() in ("1", "true", "yes"):
        return False
    try:
        import sys
        return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()
    except Exception:
        return True

def set_color_enabled(enabled):
    """Force-enable or force-disable colorized output."""
    if enabled:
        os.environ.pop("FORCE_NO_COLOR", None)
    else:
        os.environ["FORCE_NO_COLOR"] = "1"
