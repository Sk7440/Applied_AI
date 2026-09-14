import json
import os

class HistoryManager:
    """Handles saving and loading chat history to a local file."""

    def __init__(self, filename="chat_history.json"):
        self.filename = filename

    def save_history(self, messages):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(messages, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading history: {e}")
            return []

    def clear_history(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
