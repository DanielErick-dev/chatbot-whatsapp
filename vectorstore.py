import os
import shutil
from config import RAG_FILES_DIR, VECTOR_STORE_PATH
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def load_documents():
    docs = []

    files = [
        os.path.join(RAG_FILES_DIR, f)
        for f in os.listdir(RAG_FILES_DIR)
        if f.lower().endswith(('.pdf', '.txt'))
    ]

    for file in files:
        loader = PyPDFLoader(file) if file.endswith('.pdf') else TextLoader(file)
        loaded_docs = loader.load()
        for doc in loaded_docs:
            doc.metadata["source"] = file
        docs.extend(loaded_docs)

    return docs


def _move_to_processed(docs):
    processed_dir = os.path.join(RAG_FILES_DIR, 'processed')
    os.makedirs(processed_dir, exist_ok=True)

    for doc in docs:
        source = doc.metadata.get("source")
        if source and os.path.exists(source):
            shutil.move(source, os.path.join(processed_dir, os.path.basename(source)))


def get_vectorstore():
    index_file = os.path.join(VECTOR_STORE_PATH, "index.faiss")
    embedding = OpenAIEmbeddings()
    vectorstore = None

    if os.path.exists(index_file):
        vectorstore = FAISS.load_local(
            VECTOR_STORE_PATH,
            embedding,
            allow_dangerous_deserialization=True
        )

        docs = load_documents()
        if docs:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            splits = text_splitter.split_documents(docs)
            vectorstore.add_documents(splits)
            vectorstore.save_local(VECTOR_STORE_PATH)
            _move_to_processed(docs)

    else:
        docs = load_documents()
        if docs:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            splits = text_splitter.split_documents(docs)
            vectorstore = FAISS.from_documents(
                documents=splits,
                embedding=embedding
            )
            vectorstore.save_local(VECTOR_STORE_PATH)
            _move_to_processed(docs)
        else:
            print("⚠️ Nenhum documento encontrado para criar vectorstore.")

    return vectorstore
