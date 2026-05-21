import streamlit as st

st.title("AI Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    response = f"You said: {user_input}"
    st.write(response)