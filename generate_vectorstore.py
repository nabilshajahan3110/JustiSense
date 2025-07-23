from modules.rag_engine import load_docs, build_vectorstore, save_vectorstore

pdf_folder_path = "data"  # All PDFs are inside this folder

print("🔄 Loading all legal PDFs...")
docs = load_docs(pdf_folder_path)

print("🔨 Building FAISS vectorstore...")
vectorstore = build_vectorstore(docs)

print("💾 Saving vectorstore to data/vectorstore.pkl")
save_vectorstore(vectorstore)

print("✅ Vectorstore successfully created and saved!")