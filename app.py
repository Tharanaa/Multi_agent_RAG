import streamlit as st
from multiagent_rag import ask_question

st.set_page_config(
    page_title="Multi-Agent RAG",
    layout="centered"
)

st.title("🤖 Multi-Agent RAG Assistant")

question = st.text_input("Ask your question")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            answer = ask_question(question)

        st.subheader("Answer")
        st.write(answer)
