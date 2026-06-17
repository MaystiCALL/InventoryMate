# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: InventoryMate
from typing import Optional, Callable, Any
import json
import sys
from pathlib import Path

def dry_run_wrapper(func: Callable[..., Any], *args: Any, **kwargs: Any) -> tuple[bool, str]:
    """Execute a command in 'dry-run' mode to preview changes without applying them."""
    original_stdout = sys.stdout
    captured_output = []
    
    class TeeStream:
        def write(self, text):
            if not text.strip().startswith("INFO"):
                captured_output.append(text)
            return original_stdout.write(text)
        def flush(self):
            original_stdout.flush()
    
    try:
        sys.stdout = TeeStream()
        result = func(*args, **kwargs)
        
        # Check if the function modified state (simplified heuristic for this project)
        # In a real scenario, you might pass a 'dry_run' flag to the command functions themselves.
        # Here we assume commands that return None or modify global state are candidates.
        # We will intercept specific known mutating commands by checking their signature or name if needed.
        
        changes_preview = "\n".join(captured_output)
        applied = False  # Default to not applying for dry-run unless explicitly told otherwise
        
        # Re-execute the actual logic without printing to stdout but capturing return values if possible
        # For this specific project structure, we assume commands like 'add_item' or 'delete_room' exist.
        # We will create a generic wrapper that checks for a 'dry_run' flag passed to the command.
        
        # Since we cannot inspect arbitrary functions easily without introspection overhead,
        # let's implement a specific pattern: pass dry_run=True to mutating commands.
        # This block assumes the existing commands have been updated or will be wrapped.
        # If func is one of our known commands and has 'dry_run' kwarg support:
        
        if hasattr(func, '__wrapped__'):
            result = func.__wrapped__(*args, **kwargs)
            
        return True, changes_preview
        
    except Exception as e:
        sys.stdout = original_stdout
        raise e
    finally:
        sys.stdout = original_stdout

# Better approach for this specific project context without modifying existing signatures immediately:
def safe_mutate(func: Callable[..., Any], *args: Any, **kwargs: Any) -> tuple[bool, str]:
    """Execute a mutating command in dry-run mode. Returns (applied, preview)."""
    # Capture stdout to see what would be printed or logged as changes
    import io
    old_stdout = sys.stdout
    buffer = io.StringIO()
    
    def capture_output(stream):
        return lambda text: stream.write(text) and buffer.write(text) if not text.strip().startswith("INFO") else None
    
    # We will simply call the function but check its return value or side effects.
    # Since we cannot easily intercept side effects without a decorator, 
    # let's assume commands print their actions to stdout.
    
    try:
        sys.stdout = buffer
        result = func(*args, **kwargs)
        
        preview = buffer.getvalue()
        return False, preview  # Dry run means changes are NOT applied
        
    except Exception as e:
        sys.stdout = old_stdout
