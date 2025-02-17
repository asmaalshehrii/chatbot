import streamlit as st
import requests

# Backend API URL (Update if necessary)
API_URL = "https://chatbot-1-zisg.onrender.com/chat"

# 🎨 Custom Styling with CSS
st.markdown(
    """
    <style>
    body {
        background-color: #F0F2F6;
    }
    .stChatMessage {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .stChatMessage.user {
        background-color: #DCF8C6; /* Light green for user */
        text-align: left;
    }
    .stChatMessage.assistant {
        background-color: #E0E0E0; /* Light grey for bot */
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎤 Title and Description
st.markdown("<h1 style='text-align: center;'>🤖 OpenAI Chatbot</h1>", unsafe_allow_html=True)
st.write("💬 Chat with an AI-powered bot.")

# 🗂️ Session State for Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 📜 Display previous messages in chat format
for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.write(content)

# ✍️ User Input Box with Placeholder
user_input = st.text_input("Type your message...", key="user_input", placeholder="Ask me anything...")

# 🚀 Send Button for Chat
if st.button("Send 🚀", use_container_width=True):
    if user_input.strip():
        # Save user message to chat history
        st.session_state["messages"].append(("user", user_input))

        # 🎯 API Request
        response = requests.post(API_URL, json={"message": user_input})
        
        if response.status_code == 200:
            bot_response = response.json().get("response", "🤖 I couldn't process that request.")
        else:
            bot_response = f"⚠️ Error: {response.status_code}"

        # Save bot response to chat history
        st.session_state["messages"].append(("assistant", bot_response))
        
        # 🔄 Refresh UI
        st.rerun()
