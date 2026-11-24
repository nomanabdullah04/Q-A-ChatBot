import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from footer import render_footer

load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A ChatBot with GroqAI"

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Give the answer according to the queries."),
    ("user", "Question: {question}")
])

def generate_response(question, api_key, engine, temperature, max_token):
    llm = ChatGroq(
        model=engine,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_token
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"question": question})

# Streamlit UI
st.title("This is Q&A ChatBot")

# Sidebar Settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your API key", type="password")
engine = st.sidebar.selectbox(
    "Select the Groq AI model",
    ["openai/gpt-oss-120b", "openai/gpt-oss-20b", "qwen/qwen3.8-27b"]
)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max Token", min_value=50, max_value=1000, value=250)

# Main Area
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if st.button("Submit"):
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Generating response..."):
                response = generate_response(user_input, api_key, engine, temperature, max_token)
            st.subheader("Result:")
            st.info(response)  # Displays the answer inside a styled result box
        except Exception as e:
            st.error(f"Error: {e}")


render_footer()