from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import system_prompt
import os

# Initialize Flask
app = Flask(__name__)

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize embeddings
embeddings = download_hugging_face_embeddings()

# Pinecone index name
index_name = "medibot"

# Connect to existing Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
)

# Create retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Initialize LLM
llm = OpenAI(temperature=0.4, max_tokens=500)

# Prompt templates
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# Build chains
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Routes
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form.get("msg")
    print("User:", msg)
    response = rag_chain.invoke({"input": msg})
    print("Bot:", response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
