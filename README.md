# ⚖️ JustiSense – Your Legal Rights Assistant 🇮🇳

[![Live Demo](https://img.shields.io/badge/🔗%20Live%20Demo-Streamlit-green?style=for-the-badge&logo=streamlit)](https://justisense-9cpvilhy5cdfkdnjgpdwec.streamlit.app/)

**JustiSense** is an AI-powered chatbot that helps Indian citizens get quick, reliable answers to their legal questions. Built using Retrieval-Augmented Generation (RAG), it draws information from official Indian law PDFs, including IPC, RTI, FIR, and more.

---

## 💡 Key Features

- ✅ **Ask Questions Like:**
  - "What are tenant rights in Bangalore?"
  - "How to file an FIR online in Kerala?"
  - "What are my rights as a consumer?"

- 📚 **Backed by Official PDFs**
  - Indian Penal Code (IPC)
  - Right to Information (RTI) Act
  - Consumer Protection Act
  - FIR guidelines, Traffic Rules, Cyber Crime laws, etc.

- 🧠 **Stack Used**
  - LangChain + RAG pipeline
  - Groq (`llama3-8b-8192`)
  - FAISS VectorStore
  - Hugging Face Embeddings
  - Streamlit for frontend
  - Python + secrets.toml-based configuration

---

## 🖼️ Screenshots

| Profile Setup | Sample Query |
|---------------|--------------|
| ![Profile](https://i.imgur.com/HbEtI3w.png) | ![Query](https://i.imgur.com/2YzGyj9.png) |

---

## 🛠️ How it Works

1. Load official law PDFs
2. Chunk and embed them using HuggingFace + FAISS
3. Accept user query + basic location/legal area
4. Retrieve relevant chunks using similarity search
5. Feed context to LLaMA3 model via Groq
6. Streamlit renders response + sources

---

## 🧠 Ideal For

- Students learning about the law
- Citizens needing awareness of rights
- Legal tech enthusiasts
- NGOs creating public awareness tools

---

## 📦 Setup Locally

```bash
git clone https://github.com/your-username/JustiSense.git
cd JustiSense

# Set your GROQ API Key
echo "GROQ_API_KEY = 'your_api_key_here'" > .streamlit/secrets.toml

# Install requirements
pip install -r requirements.txt

# Build Vectorstore
python generate_vectorstore.py

# Run app
streamlit run JustiSense_app.py
