

import streamlit as st

st.title("🤖 AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Type your message...")

# Save user message
if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Bot response
    if "hello" in user_input.lower():
        bot_reply = "Hello 👋 How can I help you?"
    elif "python" in user_input.lower():
        bot_reply = "Python is a powerful programming language 🚀"
    elif "ai" in user_input.lower():
        bot_reply = "AI means Artificial Intelligence 🤖"
    else:
        bot_reply = "Sorry, I don't understand."

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

# Display chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])