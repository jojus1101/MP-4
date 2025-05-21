import streamlit as st
from webutils import load_web_page, split_web_text, store_web_docs, retrieve_docs, answer_question

st.title("Chat with Web Pages")

# Input URL from user
url = st.text_input("Enter a webpage URL:")

if url:
    with st.spinner("Loading and processing webpage..."):
        # Load the webpage and split it into chunks
        docs = load_web_page(url)
        chunks = split_web_text(docs)
        
        # Store the chunks in the vector store
        store_web_docs(chunks)
        
        st.success(f"Loaded {len(chunks)} chunks from the webpage.")

    # User question input
    question = st.chat_input("Ask a question about the webpage content:")

    if question:
        st.chat_message("user").write(question)
        
        # Retrieve relevant chunks and generate answer
        related_docs = retrieve_docs(question)
        answer = answer_question(question, related_docs)
        
        st.chat_message("assistant").write(answer)
