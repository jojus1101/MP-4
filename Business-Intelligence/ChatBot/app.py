import streamlit as st
import os
from utils import (
    upload_pdf, parse_pdf, split_pdf_text,
    store_pdf_docs, retrieve_docs, answer_question
)

# Directories
data = './data/'
media = './media/'

# Ensure directories exist
os.makedirs(data, exist_ok=True)
os.makedirs(media, exist_ok=True)

# Title
st.title("📄💬 Talk with Multimodal PDF")

# PDF Upload
uploaded_file = st.file_uploader(
    "📎 Upload a PDF file",
    type="pdf",
    accept_multiple_files=False
)

if uploaded_file:
    # Save and parse file
    file_path = os.path.join(data, uploaded_file.name)
    upload_pdf(uploaded_file)
    text = parse_pdf(file_path, media)
    chunks = split_pdf_text(text)
    store_pdf_docs(chunks)

    # Ask a question
    question = st.chat_input("Ask something about your PDF...")

    if question:
        st.chat_message("user").write(question)
        relevant_docs = retrieve_docs(question)
        answer = answer_question(question, relevant_docs)
        st.chat_message("assistant").write(answer)
else:
    st.info("Please upload a PDF file to start chatting with it.")
