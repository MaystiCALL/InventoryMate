# === Stage 19: Add undo support for the last simple mutation ===
# Project: InventoryMate
class UndoManager:
    def __init__(self, max_history=10):
        self.history = []
        self.max_history = max_history

    def record(self, action_type, data):
        if len(self.history) >= self.max_history:
            self.history.pop(0)
        self.history.append({'type': action_type, 'data': data})

    def undo(self):
        if not self.history:
            return None
        last = self.history.pop()
        return {'action': last['type'], 'payload': last['data']}
