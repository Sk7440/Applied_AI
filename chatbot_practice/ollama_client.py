import ollama
import logging
from typing import List, Generator, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OllamaConnectionError(Exception):
    """Raised when the Ollama server is unreachable."""
    pass

class OllamaClient:
    """Handles interactions with the local Ollama server."""

    def __init__(self, default_model: str = "gemma4:31b-cloud"):
        self.default_model = default_model

    def get_available_models(self) -> List[str]:
        """Fetches a list of all locally installed Ollama models."""
        try:
            response = ollama.list()
            if isinstance(response, dict) and 'models' in response:
                return [m['name'] for m in response['models']]
            elif isinstance(response, list):
                return [m['name'] for m in response]
            return []
        except Exception as e:
            logger.error(f"Ollama connection failure: {e}")
            raise OllamaConnectionError(f"Could not connect to Ollama server: {e}")

    def is_multimodal(self, model: str) -> bool:
        """Checks if the specified model supports multimodal inputs (images)."""
        try:
            info = ollama.show(model)
            details = str(info).lower()
            return "vision" in details or "multimodal" in details
        except Exception as e:
            logger.debug(f"Multimodal check failed for model {model}: {e}")
            return False

    def chat_stream(self, messages: List[dict], model: Optional[str] = None, images: Optional[List[bytes]] = None) -> Generator[str, None, None]:
        """
        Generates a streaming response from the specified Ollama model.
        Images are correctly attached to the last user message as per the Ollama API.
        """
        target_model = model or self.default_model
        try:
            processed_messages = []
            for i, msg in enumerate(messages):
                # Attach images to the last user message if provided
                if images and msg['role'] == 'user' and i == len(messages) - 1:
                    new_msg = msg.copy()
                    new_msg['images'] = images
                    processed_messages.append(new_msg)
                else:
                    processed_messages.append(msg)

            stream = ollama.chat(
                model=target_model,
                messages=processed_messages,
                stream=True,
            )
            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']
        except Exception as e:
            logger.error(f"Streaming error with model {target_model}: {e}")
            raise OllamaConnectionError(f"Error during chat stream with model {target_model}: {e}")
