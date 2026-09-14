import ollama
import streamlit as st

class OllamaClient:
    """Handles interactions with the local Ollama server."""

    def __init__(self, model="gemma4:31b-cloud"):
        self.model = model

    def get_available_models(self):
        try:
            models_info = ollama.list()
            if isinstance(models_info, dict) and 'models' in models_info:
                return [m['name'] for m in models_info['models']]
            elif isinstance(models_info, list):
                return [m['name'] for m in models_info]
            return []
        except Exception:
            return []

    def chat_stream(self, messages):
        """Generates a streaming response from the model."""
        try:
            stream = ollama.chat(
                model=self.model,
                messages=messages,
                stream=True,
            )
            for chunk in stream:
                yield chunk['message']['content']
        except Exception as e:
            yield f"Error: {str(e)}"
