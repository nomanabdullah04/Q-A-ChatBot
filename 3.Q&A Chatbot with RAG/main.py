import os
import glob
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.tools.tavily_search import TavilySearchResults
from style import apply_custom_theme, render_footer
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


st.set_page_config(page_title="Nexus Lab | Assistant",layout="centered")
apply_custom_theme()
load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7
)

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate respone based on the question
    <context>
    {context}
    <context>
    Question:{input}

    """

)

def create_vector_embedding():
    if "vector" not in st.session_state:
        st.session_state.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        st.session_state.loader = PyPDFDirectoryLoader("research")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=250
        )
        st.session_state.final_document = st.session_state.text_splitter.split_documents(
            st.session_state.docs
        )
        # Fixed: use st.session_state.final_document (not .document)
        st.session_state.vector = FAISS.from_documents(
            st.session_state.final_document, st.session_state.embedding
        )


st.title("RAG Document Q&A with GROQ and Huggingface")
user_prompt = st.text_input("Enter your query from the Research paper")

if st.button("Document Embedding"):
    with st.spinner("Creating vector embeddings..."):
        create_vector_embedding()
    st.success("Vector Database is ready!")

import time
if user_prompt:
    #  Fixed: check if vector exists before using it
    if "vector" not in st.session_state:
        st.warning(" Please click 'Document Embedding' first to index your PDFs.")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vector.as_retriever()
        retriever_chain = create_retrieval_chain(retriever, document_chain)

        start = time.process_time()
        response = retriever_chain.invoke({"input": user_prompt})
        st.caption(f" Response time: {time.process_time() - start:.2f}s")
        st.write(response["answer"])

        with st.expander(" Document Similarity Search"):
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("------------------")
