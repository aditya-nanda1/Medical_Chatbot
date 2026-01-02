# 🩺 Medical Chatbot – RAG Based AI Assistant

🔗 **Live Demo (Hugging Face Spaces):**  
https://huggingface.co/spaces/GodSpeeed07/medical-chatbot

---

## 📘 Project Overview

The **Medical Chatbot** is a Retrieval-Augmented Generation (RAG) based AI assistant designed to answer medical questions using trusted medical documents instead of relying on generic model knowledge.  
This approach significantly reduces hallucinations and improves response accuracy.

The chatbot retrieves relevant information from a medical book and then uses a language model to explain the answer in simple, patient-friendly language.

---

## 🧠 Architecture (Final)

### End-to-End Flow

1. **Medical Book (PDF)**  
   A trusted medical textbook is used as the knowledge source.

2. **Document Extraction**  
   Text is extracted from the PDF and cleaned for processing.

3. **Text Chunking**  
   The extracted text is split into smaller overlapping chunks to preserve context.

4. **Embeddings Generation**  
   Each chunk is converted into vector embeddings using a Sentence Transformer model.

5. **Vector Database (Knowledge Base)**  
   All embeddings are stored in **Pinecone**, enabling fast semantic similarity search.

6. **User Query Handling**  
   The user question is converted into an embedding and matched against stored vectors.

7. **Top-K Retrieval**  
   The most relevant chunks (K = 3) are retrieved from Pinecone.

8. **LLM Response Generation**  
   The retrieved context is passed to the LLM, which generates a grounded, accurate answer.

9. **Web Interface**  
   A Flask-based UI allows users to interact with the chatbot in real time.

---

## 🧱 Why RAG?

Instead of letting the model guess answers, the chatbot:
- Searches the medical document first
- Uses only relevant context
- Produces safer and more reliable medical responses

---

## ⚙️ Tech Stack

- **Python**
- **LangChain**
- **Sentence Transformers**
- **Pinecone (Vector Database)**
- **Flask**
- **Large Language Model (LLM)**
- **Hugging Face Spaces (Deployment)**

---

## ✨ Key Features

- Context-aware medical responses  
- Reduced hallucinations using RAG  
- Fast semantic search  
- Clean and modern UI  
- Scalable architecture  

---

## 🚀 Live Demo

👉 https://huggingface.co/spaces/GodSpeeed07/medical-chatbot

---

## 📌 Use Cases

- Medical Q&A assistant  
- Healthcare education  
- AI-powered reference system  
- Academic / final year AI project  

---

## 👨‍💻 Author

**Aditya Nanda**  
B.Tech CSE – AI & Data Analytics  
KIIT University  

---

⚠️ *Disclaimer: This chatbot is for educational purposes only and should not be used as a substitute for professional medical advice.*
