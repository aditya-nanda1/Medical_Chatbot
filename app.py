from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# -------------------- APP --------------------
app = Flask(__name__)
load_dotenv()

# -------------------- ENV --------------------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not PINECONE_API_KEY or not GOOGLE_API_KEY:
    raise ValueError("Missing API keys")

# -------------------- EMBEDDINGS --------------------
embeddings = download_hugging_face_embeddings()

# -------------------- PINECONE --------------------
docsearch = PineconeVectorStore.from_existing_index(
    index_name="medical-chatbot",
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}   # 🔥 VERY IMPORTANT (token saver)
)

# -------------------- GEMINI (LOW TOKEN MODE) --------------------
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash-lite",
    temperature=0.2,
    max_output_tokens=120   # 🔥 HARD LIMIT
)

# -------------------- PROMPT --------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{context}\n\nQuestion: {input}")
    ]
)

qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, qa_chain)

# -------------------- ROUTES --------------------
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]

    try:
        result = rag_chain.invoke({"input": msg})
        return result["answer"]
    except Exception as e:
        print("ERROR:", e)
        return "Service temporarily unavailable. Please try again."

# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
