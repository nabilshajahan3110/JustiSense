import streamlit as st
from modules.prompt_engine import get_legal_response
from modules.rag_engine import load_vectorstore, get_relevant_chunks

st.set_page_config(page_title="JustiSense – Your Legal Rights Advisor", layout="wide")
st.title("⚖️ JustiSense – Your Legal Rights Advisor")

with st.sidebar:
    st.header("👤 User Info (optional)")
    city = st.text_input("City", "Bangalore")
    concern_type = st.selectbox("Legal Area", ["Consumer Rights", "RTI", "Criminal Law", "Cyber Law", "Property Law"])
    user_info = f"City: {city}, Concern: {concern_type}"

    st.markdown("---")
    st.markdown("📘 Based on official Indian law documents")

with st.spinner("🔄 Loading legal knowledge base..."):
    vectorstore = load_vectorstore()

st.subheader("🗨️ Ask your legal question")
user_query = st.text_input("e.g., What are tenant rights in Bangalore?", key="query")

if user_query:
    with st.spinner("🔎 Searching legal docs..."):
        relevant_chunks = get_relevant_chunks(vectorstore, user_query)
        response = get_legal_response(user_query, user_info, relevant_chunks)
        st.success("Answer:")
        st.write(response)

    with st.expander("📚 Sources"):
        for i, chunk in enumerate(relevant_chunks, 1):
            st.markdown(f"**{i}.** {chunk.page_content.strip()[:300]}...")