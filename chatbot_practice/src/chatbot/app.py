import streamlit as st
import sys
import os

# Ensure the current directory is in the path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from ollama_client import OllamaClient
from history_manager import HistoryManager

# --- Configuration ---
st.set_page_config(
    page_title="Professional AI Assistant",
    page_icon="🧠",
    layout="wide"
)

# Define professional prompt presets
PROMPT_PRESETS = {
    "Universal Architect": """# SYSTEM PROMPT: UNIVERSAL TECHNICAL & CREATIVE ARCHITECT

## 1. CORE ROLE & PHILOSOPHY
You are an elite Senior Engineer, Technical Writer, and Code Auditor. You operate as an exceptional intellectual partner—thoughtful, precise, authoritative, and direct. You shift seamlessly across three core modes based on the user's intent:
- **Frontend Development**: Delivering production-ready, modular React TypeScript components styled with clean Tailwind CSS.
- **Technical Writing**: Explaining complex software concepts, architecture, and developer tools with absolute clarity.
- **Code Review**: Auditing existing implementations for security risks, performance bottlenecks, and structural bugs.

---

## 2. GENERAL BEHAVIORAL DIRECTIVES
- **No Conversational Filler**: Skip introductory pleasantries. Jump directly into the response.
- **Tone & Style**: Direct, professional, and intellectually curious. Speak as an expert peer without corporate buzzwords or subservience.
- **Anti-AI Tropes**: Strictly avoid generic LLM vocabulary ("delve", "tapestry", "beacon", "revolutionize").
- **First-Principles Execution**: Identify core constraints, handle edge cases proactively, and provide complete solutions without placeholders.

---

## 3. MODE SPECIFIC RULES
### Mode A: Frontend Development (React & Tailwind CSS)
- **TypeScript**: Use strict interfaces, explicit prop definitions, and modern functional hooks.
- **Styling**: Write responsive, utility-first Tailwind CSS. Use clean Flexbox/Grid structures.
- **State Coverage**: Handle loading, empty, error, and active states gracefully.
- **Format**: Lead directly with the complete component code block, followed by 2–3 bullet points on key architectural choices.

### Mode B: Technical Writing & Documentation
- **Clarity Over Jargon**: Translate abstract architecture into concrete mechanics using accurate technical terms.
- **Structure**: Use visual scaffolding—bold category headers, structured lists, and clean code snippets.
- **Actionable Focus**: Emphasize real-world usage and reproducible configuration setups.

### Mode C: Code Review & Security Audit
- **Severity-Based Triage**: Categorize findings by severity (**Critical**, **Major**, **Minor**).
- **Actionable Fixes**: Pair every flagged issue directly with its refactored code fix.
- **Final Output**: Provide a fully refactored, complete replacement file at the end.
""",
    "React/Tailwind Architect": """# SYSTEM PROMPT: ELITE FRONTEND ARCHITECT (REACT • TS • TAILWIND)

## 1. IDENTITY & CORE PHILOSOPHY
You are a world-class Staff Frontend Architect and Design Systems Engineer. Your mission is to deliver production-grade, scalable, and accessible user interfaces.

## 2. OPERATIONAL REASONING PROCESS
1. **Deconstruct Requirements**: Identify core state transitions and edge cases.
2. **Architect Component Hierarchy**: Split between container and presentational components.
3. **State Strategy**: Select most efficient state management.
4. **Accessibility Audit**: Ensure WAI-ARIA compliance.

## 3. TECHNICAL EXECUTION STANDARDS
- **Type Rigor**: Zero use of `any`. Use Discriminated Unions for complex state.
- **Modern Patterns**: Use custom hooks for logic extraction.
- **Tailwind CSS**: Use standard config classes; mobile-first responsive design.

## 4. STRICT RESPONSE DIRECTIVES
- **Zero Preamble**: Jump immediately to the code.
- **Absolute Completion**: No truncation.
- **Post-Code Analysis**: Provide a "Technical Ledger" (Architecture, Complexity, A11y).
""",
    "Standard Assistant": "You are a professional, helpful, and articulate AI assistant. Provide accurate and concise answers."
}

# Custom CSS for a high-end, production-grade "Universal Architect" Interface
st.markdown("""
    <style>
    /* Core Theme */
    .stApp {
        background-color: #0f1115;
        color: #e6edf3;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Header & Navbar */
    [data-testid="stHeader"] {
        background-color: rgba(15, 17, 21, 0);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }

    /* Chat Bubble Architecture */
    .stChatMessage {
        background-color: #1c2128;
        color: #e6edf3;
        border: 1px solid #30363d;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        padding: 1.2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: border-color 0.2s ease;
    }
    .stChatMessage:hover {
        border-color: #8b949e;
    }

    [data-testid="stChatMessageContent"] {
        color: #e6edf3 !important;
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Input Area */
    .stChatInputContainer {
        background-color: #0f1115 !important;
        border-top: 1px solid #30363d;
        padding-top: 1rem;
    }

    /* Form Elements */
    .stSelectbox label, .stTextArea label, .stMarkdown p, .stCaption {
        color: #8b949e !important;
        font-weight: 500;
    }

    /* Custom Status Indicator */
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        background-color: #238636;
        color: white;
        margin-left: 10px;
    }

    /* Typography */
    h1, h2, h3 {
        color: #f0f6fc !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize managers
history_mgr = HistoryManager()
client = OllamaClient()

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = history_mgr.load_history()
if "debug_logs" not in st.session_state:
    st.session_state.debug_logs = []

def log_debug(message):
    st.session_state.debug_logs.append(message)

# --- Sidebar ---
with st.sidebar:
    st.title("🧠 Architect Control")

    # System Health Status
    try:
        models_info = client.get_available_models()
        status_text = "SYSTEM ONLINE" if models_info else "OLLAMA OFFLINE"
        status_color = "#238636" if models_info else "#da3632"
        st.markdown(f'<div style="text-align: center;"><span class="status-badge" style="background-color: {status_color};">{status_text}</span></div>', unsafe_allow_html=True)
    except:
        st.markdown('<div style="text-align: center;"><span class="status-badge" style="background-color: #da3632;">CONNECTION ERROR</span></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Model Configuration
    st.subheader("Core Engine")
    available_models = client.get_available_models()

    if not available_models:
        st.error("No models detected. Run `ollama pull llama3`.")
        selected_model = "gemma4:31b-cloud"
    else:
        default_idx = 0
        if "gemma4:31b-cloud" in available_models:
            default_idx = available_models.index("gemma4:31b-cloud")
        selected_model = st.selectbox("Compute Model", available_models, index=default_idx)

    client.model = selected_model

    st.markdown("---")
    st.subheader("Instruction Set")

    # Preset Selector
    preset_choice = st.selectbox(
        "Persona Architecture",
        options=list(PROMPT_PRESETS.keys()),
        index=0
    )

    if "current_preset" not in st.session_state:
        st.session_state.current_preset = "Universal Architect"

    if preset_choice != st.session_state.current_preset:
        st.session_state.current_preset = preset_choice

    system_prompt = st.text_area(
        "System Constraints",
        value=PROMPT_PRESETS[preset_choice],
        help="Defines AI behavioral guardrails.",
        height=300
    )

    st.markdown("---")
    if st.button("🗑️ Purge Session", use_container_width=True):
        st.session_state.messages = []
        history_mgr.clear_history()
        st.rerun()

    st.markdown("---")
    st.subheader("🛠️ Audit Logs")
    if st.checkbox("Enable Diagnostics"):
        st.expander("Telemetry", expanded=False).write("\n".join(st.session_state.debug_logs))

st.title("Professional AI Assistant")
st.caption(f"Currently powered by **{selected_model}**")

# --- Chat Display ---
# Include system prompt in the messages sent to the API, but don't show it in the UI
api_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Interaction ---
if prompt := st.chat_input("Message your assistant..."):
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Assistant Response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # Prepare messages for API (with system prompt)
        current_api_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

        try:
            log_debug(f"Sending request to model {selected_model}...")
            for chunk in client.chat_stream(current_api_messages):
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)
            log_debug("Response received successfully.")

        except Exception as e:
            error_detail = str(e)
            log_debug(f"CRITICAL ERROR: {error_detail}")
            full_response = f"An error occurred: {error_detail}"
            st.error(full_response)
            response_placeholder.markdown(full_response)

    # 3. Save to state and disk
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    history_mgr.save_history(st.session_state.messages)
