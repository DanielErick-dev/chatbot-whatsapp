from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import (
    AI_CONTEXTUALIZE_PROMPT,
    AI__SYSTEM_PROMPT
)

contextualize_prompt = ChatPromptTemplate.from_messages({
    ('system', AI_CONTEXTUALIZE_PROMPT),
    MessagesPlaceholder('chat_history'),
    ('human', '{input}'),
})

qa_propmt = ChatPromptTemplate.from_messages({
    ('system', AI__SYSTEM_PROMPT),
    MessagesPlaceholder('chat_history'),
    ('human', '{input}')
})
