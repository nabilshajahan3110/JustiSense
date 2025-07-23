import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-8b-8192")

template = """
You are a helpful legal assistant trained in Indian law. Use the provided context to answer the user’s legal question.

User Info:
{user_info}

User's Query:
{query}

Legal Context:
{context}

Give a clear and helpful response. If unsure, say so.
"""

prompt = ChatPromptTemplate.from_template(template)

def get_legal_response(query, user_info, context_chunks):
    context = "\n\n".join(chunk.page_content for chunk in context_chunks)
    chain = prompt | llm
    return chain.invoke({
        "query": query,
        "user_info": user_info,
        "context": context
    }).content