import json
import os
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HistoryManager:
    """Handles saving and loading chat history to a local JSON file."""

    def __init__(self, filename: str = "chat_history.json"):
        self.filename = filename

    def save_history(self, messages: List[Dict[str, str]]):
        """Saves the provided message history to a JSON file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(messages, f, ensure_ascii=False, indent=4)
        except Exception as e:
            logger.error(f"Failed to save chat history: {e}")

    def load_history(self) -> List[Dict[str, str]]:
        """Loads chat history from the JSON file."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load chat history: {e}")
            return []

    def clear_history(self):
        """Deletes the chat history file."""
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except Exception as e:
            logger.error(f"Failed to clear chat history: {e}")
