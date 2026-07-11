# === Stage 61: Add performance timing for core list and search operations ===
# Project: InventoryMate
def _time(func, *args):
    import time, sys
    t = time.perf_counter()
    result = func(*args)
    elapsed_ms = (time.perf_counter() - t) * 1000
    print(f"[{sys._getframe().f_back.f_code.co_name}] {func.__name__}: {elapsed_ms:.2f} ms")
    return result

# Example usage:
# _time(list_all_items, db)
