# Local AI Assistant

A professional local AI chatbot powered by Ollama and Streamlit.

## Features
- **Local Models**: Runs entirely on your machine for privacy and speed.
- **Dynamic Model Selection**: Seamlessly switch between installed Ollama models.
- **Image Analysis**: Support for multimodal models via sidebar uploads.
- **Persistent Memory**: Session history is saved to `chat_history.json`.
- **Optimized Performance**: Limited context window for faster response times.

## Setup

1. **Install Ollama**: Visit [ollama.com](https://ollama.com) to download and install.
2. **Pull a model**: Run `ollama pull gemma4:31b-cloud` (or `llava` for vision capabilities).
3. **Install dependencies**: `pip install streamlit ollama`
4. **Run the application**: `streamlit run app.py`
