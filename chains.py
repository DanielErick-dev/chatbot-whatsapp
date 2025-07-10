from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain
)
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from config import (
    OPENAI_MODEL_NAME,
    OPENAI_MODEL_TEMPERATURE
)
from vectorstore import get_vectorstore
from prompts import contextualize_prompts, qa_prompt


def get_rag_chain():
    llm = ChatOpenAI(
        model=OPENAI_MODEL_NAME,
        temperature=OPENAI_MODEL_TEMPERATURE
    )
    retriever = get_vectorstore().as_retriever()
    history_aware_chain = create_history_aware_retriever(
        llm, retriever,
        contextualize_prompts
    )
    question_answer_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=qa_prompt
    )
    return create_retrieval_chain(
        history_aware_chain,
        question_answer_chain
    )