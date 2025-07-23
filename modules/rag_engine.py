from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import pickle
import os

def load_docs(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            documents.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)

def build_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)

def save_vectorstore(vectorstore, path="data/vectorstore.pkl"):
    with open(path, "wb") as f:
        pickle.dump(vectorstore, f)

def load_vectorstore(path="data/vectorstore.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def get_relevant_chunks(vectorstore, query, k=3):
    return vectorstore.similarity_search(query, k=k)