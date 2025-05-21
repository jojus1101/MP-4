# This is a test Streamlit app that allows users to upload a PDF document or enter a URL to load text from a web page.
# The app has issues with combining the functionalities of both PDF and web page processing.

import streamlit as st
import os
from utils import (
    upload_pdf, parse_pdf, split_pdf_text, store_pdf_docs,
    load_web_page, split_web_text, store_web_docs,
    retrieve_docs, answer_question
)

# Directories for saving files and media
data_dir = './data/'
media_dir = './media/'

st.title("Multimodal Chatbot for PDF & Web")

# --- PDF Upload Section ---
st.header("Upload a PDF Document")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=False
)

if uploaded_file:
    file_path = os.path.join(data_dir, uploaded_file.name)
    upload_pdf(uploaded_file)
    pdf_text = parse_pdf(file_path, media_dir)
    pdf_chunks = split_pdf_text(pdf_text)
    store_pdf_docs(pdf_chunks)
    st.success(f"PDF '{uploaded_file.name}' processed and stored.")

# --- Webpage URL Section ---
st.header("Load Text from a Web Page")

url_input = st.text_input("Enter a URL to load and parse")

if url_input:
    try:
        web_docs = load_web_page(url_input)
        web_chunks = split_web_text(web_docs)
        store_web_docs(web_chunks)
        st.success(f"Web page '{url_input}' loaded and stored.")
    except Exception as e:
        st.error(f"Failed to load page: {e}")

# --- Chat Interaction ---
st.header("Ask a Question")

question = st.text_input("Enter your question here:")

if question:
    related_docs = retrieve_docs(question)
    answer = answer_question(question, related_docs)
    st.markdown(f"**Answer:** {answer}")