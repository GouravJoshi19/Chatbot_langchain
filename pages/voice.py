import streamlit as st
from streamlit_lottie import st_lottie
from langchain.llms import Cohere
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage,HumanMessage
import speech_recognition as sr
import requests
import os



api_key=st.secrets.cohere_api.cohere_api_key

cohere_llm=Cohere(cohere_api_key=api_key,
           model="command-xlarge-nightly",
           temperature=0.7,
           max_tokens=250,)

system_template = "You are a helpful assistant that answers questions and engages in conversation."

prompt_1=ChatPromptTemplate.from_messages([
    SystemMessage(content=system_template),('user','{text}')
])

def generate(user_input):
  formatted_prompt=prompt_1.format(question=user_input)
  Response=cohere_llm(formatted_prompt)
  return Response


# Initialize the recognizer
r = sr.Recognizer()

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Streamlit app setup
st.title("Voice-enabled Chatbot")




# Microphone image or icon for visual cue (you can replace this with an actual image file if needed)
st.markdown('<i class="fas fa-microphone" style="font-size:48px;color:red;"></i>', unsafe_allow_html=True)

# Placeholder for status messages
status_placeholder = st.empty()

# Audio recording flag
is_recording = False

# Function to simulate audio recording
def record_audio():
    with sr.Microphone() as source:
        # Adjust for ambient noise to improve accuracy
        r.adjust_for_ambient_noise(source)
        status_placeholder.text("Recording... Speak now!")
        audio = r.listen(source)
        status_placeholder.text("Recording finished.")
        return audio

# "Start Recording" button
if st.button("Start Recording"):
    is_recording = True
    with st.spinner("Recording..."):
        # Start recording audio
        audio = record_audio()
        try:
            # Recognize speech using Google Speech Recognition
            user_input = r.recognize_google(audio)

            
            try:
                response = generate(user_input.lower())
                st.success(f"You: {user_input}")
            except:
                st.error("SomeThing Went Wrong!!")

        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition; {e}")



lottie_ai_bot = load_lottie_url("https://lottie.host/bc38a63c-7319-478c-8ed2-c92f18e4a486/6cD55ycFvN.json")
st_lottie(lottie_ai_bot, height=300, key="ai_bot")

st.warning("This Feature is still Under Development.")
