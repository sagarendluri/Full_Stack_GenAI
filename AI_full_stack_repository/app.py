from ingest import run_ingest
from llm.wrapper import setup_qa_chain
from llm.wrapper import query_embeddings
import timeit


import streamlit as st
def main():
    st.set_page_config(page_title="Document seemless process ")
    st.title("Auto text extraction with AI Planet ")
    st.subheader("I can help you in extracting text from pdf,documents ....")
    pdf = st.file_uploader("Upload text here for now, only PDF files allowed ", type=["pdf","txt"],accept_multiple_files=True)
    submit=st.button("Extract Data")
    if submit:
        with st.spinner('Wait for it...'):
            run_ingest()
    question = st.text_input("Please wirte a Query: ", key="Please ask question on uploaded pdf")
    submit = st.button('Generate') 
    if submit: 
        with st.spinner('Wait for it...'):
            qa_chain = setup_qa_chain()
            response = qa_chain({'query': question})
            answer = {'answer': response['result']}
            st.subheader("Answer:")
            st.write(answer) 
            st.success("Hope I was able to save your time❤️")
#Invoking main function
if __name__ == '__main__':
    main()
