# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: InventoryMate
def validate_required(value, field_name):
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"Field '{field_name}' cannot be empty")
    return True

def validate_identifier(value, prefix=""):
    if not isinstance(value, str):
        raise TypeError(f"Identifier must be a string")
    clean = value.strip()
    if not clean:
        raise ValueError("Identifier cannot be empty")
    if len(clean) > 64:
        raise ValueError("Identifier exceeds maximum length of 64 characters")
    if not re.match(r'^[a-zA-Z0-9_-]+$', clean):
        raise ValueError("Identifier can only contain letters, numbers, underscores, and hyphens")
    return clean

def validate_short_text(value, max_length=100):
    if not isinstance(value, str):
        raise TypeError(f"Text must be a string")
    clean = value.strip()
    if len(clean) > max_length:
        raise ValueError(f"Text exceeds maximum length of {max_length} characters")
    return clean

def validate_positive_number(value, field_name=""):
    try:
        num = float(value)
        if num <= 0:
            raise ValueError(f"{field_name or 'Value'} must be greater than zero")
        return num
    except (TypeError, ValueError):
        raise TypeError(f"{field_name or 'Value'} must be a valid number")

def validate_date_string(value):
    if not isinstance(value, str):
        raise TypeError("Date must be a string")
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_email(value):
    if not isinstance(value, str):
        raise TypeError("Email must be a string")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise ValueError("Invalid email format")
    return value

def validate_url(value):
    if not isinstance(value, str):
        raise TypeError("URL must be a string")
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    if not re.match(pattern, value):
        raise ValueError("Invalid URL format")
    return value

def validate_file_path(value):
    if not isinstance(value, str):
        raise TypeError("File path must be a string")
    if not os.path.exists(value):
        raise FileNotFoundError(f"File or directory not found: {value}")
    return value
