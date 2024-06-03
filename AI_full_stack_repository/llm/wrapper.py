import box
import yaml
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from llm.prompts import qa_template
from llm.llm import setup_llm
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain.vectorstores import Chroma
# Import config vars
with open('config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))
def set_qa_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=qa_template,
                            input_variables=['context', 'question'])
    return prompt

def build_retrieval_qa_chain(llm, prompt):    
    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2",model_kwargs={'device': 'cpu'})
    # load from disk
    chromadb = Chroma(persist_directory="./vectorestore/db_faiss", embedding_function=embedding_function)
    retriever = chromadb.as_retriever(search_kwargs={'k': cfg.VECTOR_COUNT})
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type='stuff',
                                           retriever=retriever,
                                           return_source_documents=cfg.RETURN_SOURCE_DOCUMENTS,
                                           chain_type_kwargs={'prompt': prompt})
    
    return qa_chain
def setup_qa_chain():
    llm = setup_llm()
    qa_prompt = set_qa_prompt()
    qa_chain = build_retrieval_qa_chain(llm, qa_prompt)
    return qa_chain




def query_embeddings(query):
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2",model_kwargs={'device': 'cpu'})
    chromadb = Chroma(persist_directory="./vectorestore/db_faiss", embedding_function=embedding_function)
    retriever = chromadb.as_retriever(search_kwargs={'k': cfg.VECTOR_COUNT})
    semantic_search = retriever.similarity_search_with_relevance_scores(query)
    return semantic_search