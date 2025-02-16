import streamlit as st
import requests

# FastAPI backend URL (Replace with your deployed backend URL later)
API_URL = "http://127.0.0.1:8000/chat"  # Change this if your backend is hosted online

# Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="🤖")

st.title("🤖 OpenAI Chatbot")
st.write("Talk to the chatbot powered by OpenAI.")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for message in st.session_state["messages"]:
    role, content = message
    with st.chat_message(role):
        st.write(content)

# User input
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state["messages"].append(("user", user_input))
        
        # Send request to FastAPI backend
        response = requests.post(API_URL, json={"message": user_input})
        
        if response.status_code == 200:
            bot_response = response.json().get("response", "Error: No response received.")
        else:
            bot_response = f"Error: {response.status_code}"

        # Add bot response to chat history
        st.session_state["messages"].append(("assistant", bot_response))
        
        # Clear input field
        st.experimental_rerun()
