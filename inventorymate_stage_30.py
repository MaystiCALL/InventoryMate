# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: InventoryMate
import re
from datetime import date, timedelta

def parse_date_input(text: str) -> date | None:
    """Parse common date formats with descriptive error messages."""
    if not text.strip():
        return None
    
    patterns = [
        (r'^(\d{4})-(\d{1,2})-(\d{1,2})$', lambda m: date(int(m.group(1)), int(m.group(2)), int(m.group(3)))),  # YYYY-MM-DD
        (r'^(\d{1,2})/(\d{1,2})/(\d{4})$', lambda m: date(int(m.group(3)), int(m.group(1)), int(m.group(2)))),  # MM/DD/YYYY or DD/MM/YYYY logic handled below
    ]

    for pattern, parser in patterns:
        match = re.match(pattern, text)
        if match:
            try:
                return parser(match)
            except ValueError as e:
                raise ValueError(f"Invalid date value: {text}. Error: {e}") from e
    
    # Fallback for MM/DD/YYYY vs DD/MM/YYYY ambiguity (assume US format first)
    parts = text.split('/')
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        try:
            m, d, y = map(int, parts)
            return date(y, m, d)
        except ValueError:
            pass
    
    raise ValueError(f"Unable to parse date string: '{text}'. Supported formats: YYYY-MM-DD or MM/DD/YYYY")
