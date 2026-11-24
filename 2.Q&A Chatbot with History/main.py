import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from footer import render_footer
from style import apply_custom_theme
st.set_page_config(page_title="Nexus Lab | Groq AI Chatbot", page_icon="⚡", layout="wide")
apply_custom_theme()
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A ChatBot with GroqAI"

# Prompt Template with Chat History
prompt=ChatPromptTemplate([
    ("system","Yor are helpfull assistance ,Give the queries answer accoudng to the question"),
    MessagesPlaceholder(variable_name="history"),
    ("user","{question}")
])

def generate_response(question,history,api_key,engine,temerature,max_tokens):
    llm=ChatGroq(
        model=engine,
        api_key=api_key,
        temperature=temerature,
        max_tokens=max_tokens
    )
    outputParser=StrOutputParser()
    chain=prompt|llm|outputParser
    return chain.invoke({"question":question,"history":history})

#Title
st.title("Q&A Chatbot with History")
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API key",type="password")
engine=st.sidebar.selectbox(
    "Select Groq Model",
    ["openai/gpt-oss-120b", "openai/gpt-oss-20b", "qwen/qwen3.8-27b"]
)

temerature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max_Tokens",min_value=150,max_value=1000,value=250)


#Initialiaze chat history in session state

if "messages" not in st.session_state:
    st.session_state.messages=[]

#Clear chat button in slider
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages=[]
    st.rerun()

#Dipsly the prevuious messages

for role,content in st.session_state.messages:
    with st.chat_message(role):
        st.write(content)

#Chat input box at the bottom
if user_input:=st.chat_input("Ask a question.."):
    if not api_key:
        st.warning("Please Enter your API_Key")
    else:      
        #show and save user messages
        with st.chat_message("user"):
            st.write(user_input)
        #Generate response using exiting history(before appending Input)
        with st.chat_message("assistant"):
            response=generate_response(
                user_input,st.session_state.messages,api_key,engine,temerature,max_tokens
                  )
            st.write(response)
        #Save both turns and session start

        st.session_state.messages.append(("user",user_input))
        st.session_state.messages.append(("assistant",response))






























render_footer()