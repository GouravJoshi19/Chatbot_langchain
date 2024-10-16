import streamlit as st
from langchain.llms import Cohere
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage,HumanMessage
import speech_recognition as sr

import os
st.set_page_config(page_title="Interactive Chatbot", layout="wide")

api_key=st.secrets.cohere_api.cohere_api_key
cohere_llm=Cohere(cohere_api_key=api_key,
           model="command-xlarge-nightly",
           temperature=0.7,
           max_tokens=250,)


st.title("Chatbot Web App")
st.write("### Ask me anything!")



system_template = "You are a helpful assistant who answers the questions thoughtfully."


prompt_1=ChatPromptTemplate([
    ('system',system_template),('user','{question}')
])

def generate(user_input):
  formatted_prompt=prompt_1.format(question=user_input)
  Response=cohere_llm(formatted_prompt)
  return Response


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


# Button to submit the input
if user_input := st.chat_input():
    if not user_input:
        st.error("Please Ask Something.")
       
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})
        try:  
            st.chat_message("user").write(user_input)
            with st.spinner("Creating a response"): # Get the chatbot's response
                response=generate(user_input)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.chat_message("assistant").write(response)

        except:
            st.error("Something Went Wrong.")