# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

*All commands should be run from the repository root.*

### Chatbot Practice (Main Project)
- **Install dependencies**: `pip install streamlit ollama`
- **Run application**: `streamlit run chatbot_practice/app.py`
- **Model Setup**:
  - Install Ollama from [ollama.com](https://ollama.com)
  - Pull model: `ollama pull gemma4:31b-cloud`

### Ai App
- **Run**: `python Ai_App/main.py`

## Architecture & Structure

The repository contains multiple AI experimentation projects. The primary project is `chatbot_practice`.

### chatbot_practice
A local AI assistant built with Streamlit and Ollama.
- `app.py`: Entry point. Handles the Streamlit UI, session state, and integrates the client and history manager.
- `ollama_client.py`: `OllamaClient` class. Encapsulates interactions with the local Ollama server, including streaming chat and multimodal capability checks.
- `history_manager.py`: `HistoryManager` class. Manages persistent chat history using a local `chat_history.json` file.

### Ai_App
A minimal project scaffold.
- `main.py`: Simple entry point.
- `src/ai_app/__init__.py`: Contains the `main()` function for the `ai-app` script defined in `pyproject.toml`.
