import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="AI ChatBot Home",
    page_icon="🤖",
    layout="centered",
)

# Function to load Lottie animation filessss
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animations URL
lottie_ai_bot = load_lottie_url("https://lottie.host/5e56f0b9-2154-4a33-8ce7-fc17706686fb/PyVJYjDeyU.json")
lottie_hello = load_lottie_url("https://lottie.host/2db58ef1-e369-4b1d-bb02-2879c3151432/jFVQjVv0JU.json")

# Setting the page configuration

# Home page content
st.title("Welcome to AI ChatBot App! 🤖")

st.subheader("Your Personal Conversational Assistant")
st.write("""
This chatbot app helps you interact using either text or voice! Whether you're here to chat or ask questions, 
our AI model is ready to assist you. Feel free to explore the app and experience the power of modern conversational AI!
""")

# Lottie Animation for AI
st_lottie(lottie_ai_bot, height=300, key="ai_bot")

# Adding more information
st.write("""
### What can this AI do?
- **Answer your questions**: Ask anything, and the chatbot will provide a response.
- **Voice interaction**: Speak instead of typing, and the chatbot will recognize your voice.
- **Dynamic learning**: The AI model uses state-of-the-art techniques to generate responses based on input.
""")

# Lottie Animation for Hello Greeting
st_lottie(lottie_hello, height=200, key="hello")

# Information about using the app
st.write("""
#### How to use:
1. **Switch to the Chat page**: Type your questions or commands.
2. **Switch to the Voice Bot page**: Use your microphone to talk to the AI.
3. **Enjoy an interactive and friendly conversation!**
""")

# Optional footer section
st.write("### Ready to explore? Head to the chat or voice bot sections now!")


