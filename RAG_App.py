import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.core.prompts import ChatPromptTemplate
from langchain.community.vectorsstores import FAISS
from langchain.community.document_loaders import PyPDFLoader
from langchain.huggingface import HuggingFaceEmbeddings
import time

# Load environment variables
load_dotenv()

# Set up Groq API key
# groq_api_key = os.getenv("GROQ_API_KEY")
groq_api_key = st.secrets["GROQ_API_KEY"]
st.set_page_config(page_title="Dynamic RAG with Groq",layout="width")
st.image("genetic_ai")
st.title("Dynamic RAG with Groq, FAISS , and Llama3")
if "vector"not in st.sessio_state;
   st.session_state.vector=None
if "chat_history" not in st.session_state:
  st.session_state.chat_history=[]
with st.sidebar:
  st.header("Upload Documents")
  uploaded_files=st.uploader("Upload your PDF documents", type="pdf", accept_multiple_files=True)
if st.button("Process Documents"):
  if uploaded_filefs:
    with st.spinner("processing documents.."):
    docs=[]
    for file in upload_files:
      with open(file.name,"web") as f:
        f.write=file.getbuffer())
        






