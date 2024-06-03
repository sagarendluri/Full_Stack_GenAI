# from langchain.vectorstores import Chroma
# # from langchain_chroma import Chroma
# from langchain_community.document_loaders import TextLoader
# from langchain_community.embeddings.sentence_transformer import (
#     SentenceTransformerEmbeddings,
# )
# from langchain.document_loaders import PyPDFDirectoryLoader 
# from langchain_text_splitters import CharacterTextSplitter
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import os
# os.getcwd()

# #Load Documents
# def file_loader(filename):
#     if filename.endswith('.txt'):
#         # load the text document and split it into chunks
#         loader = TextLoader(filename)
#         documents = loader.load()
#         return documents
#     #Loads pdf files available in a directory with pypdf
#     elif filename.endswith('.pdf'):
#         loader = PyPDFDirectoryLoader(filename)
#         documents = loader.load()
#         return documents
# filename = '/data'
# def load_docs(directory):
#     loader = PyPDFDirectoryLoader(directory)
#     documents = loader.load()
#     if not documents:
#         raise ValueError(f"No documents loaded from directory: {directory}")
#     return documents
# documents = load_docs(filename)
# print(f"Number of loaded documents: {len(documents)}")

# # split it into chunks
# def split_docs(documents, chunk_size=2000, chunk_overlap=20):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
#     docs = text_splitter.split_documents(documents)
#     if not docs:
#         raise ValueError("Document splitting resulted in an empty list.")
#     return docs
# docs = split_docs(documents)
# print(f"Number of document chunks: {len(docs)}")


# # Generate text embeddings
# #Huggingface LLM for creating Embeddings for documents/text

# # create the open-source embedding function
# embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2",model_kwargs={'device': 'cpu'})

# # load it into Chroma
# db = Chroma.from_documents(docs, embedding_function)

# # query it
# query = "What is invoice number?"
# docs = db.similarity_search(query)

# # print results
# print(docs[0].page_content)

#---------------------------------------------------------PDF-READER------------------------------------------------------------------
# import easyocr
# reader = easyocr.Reader(['en'])
# result = reader.readtext(r'/Users/hemasagarendluri1996/llm-mistral-invoice-cpu/screenshot_images/invoice_image.png')
# for detection in result:
#     print(detection[1])
import streamlit as st

#Hello! It seems like you want to import the Streamlit library in Python. Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
#Once you have Streamlit installed, you can import it into your Python script using the import statement,
def main():

    st.set_page_config(page_title="Document seemless process ")
    st.title("Auto text extraction with AI Planet ")
    st.subheader("I can help you in extracting text from pdf,documents ....")


    # Upload the Invoices (pdf files)...
    pdf = st.file_uploader("Upload invoices here for now, only PDF files allowed and will accept other formate as well", type=["pdf"],accept_multiple_files=True)

    submit=st.button("Extract Data")
    response = 4+5
    if submit:
        with st.spinner('Wait for it...'):
            st.subheader("Answer:")
        st.write(response)




#Invoking main function
if __name__ == '__main__':
    main()
