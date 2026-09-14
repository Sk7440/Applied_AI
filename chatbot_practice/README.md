# Professional AI Chatbot

A production-ready local AI interface built with Streamlit and Ollama.

## 🚀 Professional Architecture
This project follows a modular design:
- `src/chatbot/app.py`: The UI layer (Streamlit).
- `src/chatbot/ollama_client.py`: The AI integration layer (Ollama API).
- `src/chatbot/history_manager.py`: The persistence layer (JSON storage).

## ✨ Advanced Features
- **Personality Control**: Custom a system prompt in the sidebar to change the AI's behavior.
- **Persistent Memory**: Chat history is saved to `chat_history.json` and persists across browser refreshes.
- **Dynamic Model Switching**: Switch between any locally installed Ollama models on the fly.
- **Streaming Output**: Real-time response generation for a natural feel.

## 🛠️ Setup & Execution

### 1. Prerequisites
- [Ollama](https://ollama.com) installed and running.
- Pull the recommended model:
  ```bash
  ollama pull gemma4:31b-cloud
  ```

### 2. Install Dependencies
```bash
pip install streamlit ollama
```

### 3. Run the Application
Use the following command to launch the professional interface:
```bash
streamlit run src/chatbot/app.py
```

## 📁 Project Structure
```text
chatbot_practice/
├── src/
│   └── chatbot/
│       ├── __init__.py
│       ├── app.py             # Main UI
│       ├── ollama_client.py    # AI Logic
│       └── history_manager.py   # Storage Logic
├── pyproject.toml
└── README.md
```
