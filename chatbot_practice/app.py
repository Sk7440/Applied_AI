import streamlit as st
from ollama_client import OllamaClient, OllamaConnectionError
from history_manager import HistoryManager

# --- Configuration & Page Setup ---
DEFAULT_SYSTEM_PROMPT = {
    "Quick": "You are a helpful, professional, and extremely concise AI assistant. Provide direct answers.",
    "Balanced": "You are a helpful, professional, and balanced AI assistant. Provide clear and comprehensive answers.",
    "Deep": "You are a professional AI expert. Think step-by-step, provide exhaustive reasoning, and ensure absolute accuracy."
}

st.set_page_config(
    page_title="AI Workspace",
    page_icon=None,
    layout="wide"
)

# --- Theme Management ---
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def get_theme_css():
    if st.session_state.theme == "dark":
        return {
            "bg_primary": "#000000",
            "bg_secondary": "#171717",
            "bg_surface": "#212121",
            "text_primary": "#ffffff",
            "text_muted": "#8e8e93",
            "border_color": "#333333",
            "accent_color": "#2b7fff",
            "accent_glow": "rgba(43, 127, 255, 0.25)",
            "avatar_bg": "#333333",
            "avatar_text": "#ffffff"
        }
    else:
        return {
            "bg_primary": "#ffffff",
            "bg_secondary": "#f5f5f7",
            "bg_surface": "#e8e8e8",
            "text_primary": "#000000",
            "text_muted": "#6e6e73",
            "border_color": "#d1d1d6",
            "accent_color": "#0066cc",
            "accent_glow": "rgba(0, 102, 204, 0.1)",
            "avatar_bg": "#ddd",
            "avatar_text": "#000000"
        }

# --- Sidebar & Theme Initialization ---
# To ensure theme changes apply immediately to the CSS, we define the toggle before applying styles.
# However, Streamlit executes top-to-bottom. We'll use a small trick:
# The toggle is in the sidebar, but we need the color values for the CSS block above.
# We'll check the session state, and if the toggle is clicked, the app reruns.

colors = get_theme_css()

# --- Professional Designer CSS (Skills.md Standard) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Main Canvas */
    .stApp {{
        background-color: {colors['bg_primary']} !important;
        color: {colors['text_primary']} !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {colors['bg_secondary']} !important;
        border-right: 1px solid {colors['border_color']} !important;
    }}

    /* Chat Messages */
    .stChatMessage {{
        background-color: {colors['bg_surface']} !important;
        color: {colors['text_primary']} !important;
        border: 1px solid {colors['border_color']} !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* Chat Input Pill Approximation */
    .stChatInputContainer {{
        padding-bottom: 2rem !important;
    }}
    [data-testid="stChatInput"] {{
        background-color: {colors['bg_surface']} !important;
        border: 1px solid {colors['border_color']} !important;
        border-radius: 9999px !important;
        color: {colors['text_primary']} !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    [data-testid="stChatInput"]:focus-within {{
        border-color: {colors['accent_color']} !important;
        box-shadow: 0 0 20px {colors['accent_glow']} !important;
    }}

    /* Typography Scale */
    h1 {{
        font-size: 24px !important;
        line-height: 1.4 !important;
        font-weight: 500 !important;
        color: {colors['text_primary']} !important;
    }}
    h2 {{
        font-size: 18px !important;
        line-height: 1.3 !important;
        font-weight: 600 !important;
        color: {colors['text_primary']} !important;
    }}
    .stMarkdown p {{
        font-size: 14px !important;
        line-height: 1.4 !important;
        color: {colors['text_muted']} !important;
    }}
    .stSelectbox label, .stTextArea label {{
        font-size: 14px !important;
        color: {colors['text_muted']} !important;
    }}

    /* Sidebar Navigation Styling */
    .nav-item {{
        display: block;
        padding: 8px 12px;
        color: {colors['text_muted']} !important;
        text-decoration: none !important;
        font-size: 14px;
        border-radius: 8px;
        transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .nav-item:hover {{
        background-color: {colors['bg_surface']};
        color: {colors['text_primary']} !important;
    }}
    .badge {{
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        background: #262626;
        color: #fff;
        padding: 2px 6px;
        border-radius: 4px;
        margin-left: 8px;
    }}

    /* Remove default Streamlit header/footer */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- Professional Designer CSS (Skills.md Standard) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Main Canvas */
    .stApp {{
        background-color: {colors['bg_primary']};
        color: {colors['text_primary']};
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {colors['bg_secondary']};
        border-right: 1px solid {colors['border_color']};
    }}

    /* Chat Messages */
    .stChatMessage {{
        background-color: {colors['bg_surface']} !important;
        color: {colors['text_primary']} !important;
        border: 1px solid {colors['border_color']} !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* Chat Input Pill Approximation */
    .stChatInputContainer {{
        padding-bottom: 2rem !important;
    }}
    [data-testid="stChatInput"] {{
        background-color: {colors['bg_surface']} !important;
        border: 1px solid {colors['border_color']} !important;
        border-radius: 9999px !important;
        color: {colors['text_primary']} !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    [data-testid="stChatInput"]:focus-within {{
        border-color: {colors['accent_color']} !important;
        box-shadow: 0 0 20px {colors['accent_glow']} !important;
    }}

    /* Typography Scale */
    h1 {{
        font-size: 24px !important;
        line-height: 1.4 !important;
        font-weight: 500 !important;
        color: {colors['text_primary']} !important;
    }}
    h2 {{
        font-size: 18px !important;
        line-height: 1.3 !important;
        font-weight: 600 !important;
        color: {colors['text_primary']} !important;
    }}
    .stMarkdown p {{
        font-size: 14px !important;
        line-height: 1.4 !important;
        color: {colors['text_muted']} !important;
    }}
    .stSelectbox label, .stTextArea label {{
        font-size: 14px !important;
        color: {colors['text_muted']} !important;
    }}

    /* Sidebar Navigation Styling */
    .nav-item {{
        display: block;
        padding: 8px 12px;
        color: {colors['text_muted']} !important;
        text-decoration: none !important;
        font-size: 14px;
        border-radius: 8px;
        transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .nav-item:hover {{
        background-color: {colors['bg_surface']};
        color: {colors['text_primary']} !important;
    }}
    .badge {{
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        background: #262626;
        color: #fff;
        padding: 2px 6px;
        border-radius: 4px;
        margin-left: 8px;
    }}

    /* Remove default Streamlit header/footer */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- Initialize Components ---
client = OllamaClient()
history_mgr = HistoryManager()

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = history_mgr.load_history()

# --- Sidebar ---
with st.sidebar:
    st.title("Configuration")

    # Theme Toggle
    is_light = st.toggle("Light Mode", value=(st.session_state.theme == "light"))
    st.session_state.theme = "light" if is_light else "dark"
    if st.session_state.theme != "dark" and not is_light: # Ensure state consistency
         st.session_state.theme = "dark"

    st.markdown("---")

    # Reasoning Depth Selection
    reasoning_depth = st.select_slider(
        "Reasoning Depth",
        options=["Quick", "Balanced", "Deep"],
        value="Balanced"
    )

    try:
        available_models = client.get_available_models()
        if not available_models:
            selected_model = "gemma4:31b-cloud"
        else:
            default_idx = 0
            if "gemma4:31b-cloud" in available_models:
                default_idx = available_models.index("gemma4:31b-cloud")
            selected_model = st.selectbox("Model Selection", available_models, index=default_idx)
    except OllamaConnectionError as e:
        st.error(f"Connection Error: {e}")
        selected_model = "gemma4:31b-cloud"

    st.markdown("---")

    # Workspace Modules (Professional Navigation)
    st.subheader("Workspace")
    st.markdown('<a class="nav-item" href="#">Images <span class="badge">Updated</span></a>', unsafe_allow_html=True)
    st.markdown('<a class="nav-item" href="#">Library</a>', unsafe_allow_html=True)
    st.markdown('<a class="nav-item" href="#">Canvas Workspace</a>', unsafe_allow_html=True)
    st.markdown('<a class="nav-item" href="#">Projects</a>', unsafe_allow_html=True)

    st.markdown("---")

    # Image Upload Section
    st.subheader("Visual Analysis")
    uploaded_file = st.file_uploader("Attach image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        if not client.is_multimodal(selected_model):
            st.warning(f"Notice: Model **{selected_model}** may not support vision. Try `llava`.")

    st.markdown("---")

    if st.button("Clear Session", use_container_width=True):
        st.session_state.messages = []
        history_mgr.clear_history()
        st.rerun()

    # Profile Footer
    st.markdown("---")
    st.markdown(f"""
        <div style='display: flex; align-items: center; gap: 10px; margin-bottom: 10px;'>
            <div style='background: {colors['avatar_bg']}; color: {colors['avatar_text']}; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 12px;'>SK</div>
            <div style='color: {colors['text_primary']};'>
                <div style='font-weight: 500; font-size: 14px;'>Sultan Khalid</div>
                <div style='font-size: 12px; color: {colors['text_muted']};'>Pro</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Claim offer", use_container_width=True)

# --- Main Interface ---
if not st.session_state.messages:
    st.markdown(f"""
        <div style='text-align: center; margin-top: 15vh;'>
            <h1 style='font-size: 48px; margin-bottom: 10px;'>Ready when you are.</h1>
            <p style='color: {colors['text_muted']}; font-size: 18px;'>Your professional AI workspace is active.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.title("AI Workspace")
    st.caption(f"Active Model: **{selected_model}** | Depth: **{reasoning_depth}** via Ollama")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # Optimizations: Reasoning depth based on slider + Limit context to last 10 messages
        recent_messages = st.session_state.messages[-10:]
        api_messages = [{"role": "system", "content": DEFAULT_SYSTEM_PROMPT[reasoning_depth]}] + recent_messages

        image_bytes = [uploaded_file.getvalue()] if uploaded_file else None

        try:
            for chunk in client.chat_stream(api_messages, model=selected_model, images=image_bytes):
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error: {e}"
            st.error(full_response)
            response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    history_mgr.save_history(st.session_state.messages)
