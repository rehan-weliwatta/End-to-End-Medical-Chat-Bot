# End-to-End-Medical-Chat-Bot
🩺 Suwa Setha AI – End‑to‑End Medical Chatbot
An intelligent healthcare assistant built with Flask, LangChain, OpenAI, Hugging Face embeddings, and Pinecone vector storage.
This project demonstrates how to integrate modern LLMs with document retrieval to provide context‑aware medical information in a conversational interface.

✨ Features
🤖 Interactive Chat UI – Clean frontend built with HTML, CSS, and JavaScript.

📚 PDF Knowledge Base – Upload and process medical documents using PyPDFLoader and DirectoryLoader.

🧠 Embeddings – Hugging Face sentence transformers for semantic search.

🔎 Vector Search – Pinecone index for fast and scalable retrieval.

🗣️ Conversational AI – OpenAI LLM integrated via LangChain for natural responses.

⚡ RAG Pipeline – Retrieval‑Augmented Generation combining context from documents with LLM answers.

📊 Extensible Dashboard – Ready to connect analytics and monitoring for usage insights.

🌐 Flask Backend – REST endpoints for chat and dashboard integration.

🚀 Tech Stack
Backend: Flask, Python

Frontend: HTML, CSS, JavaScript

AI/ML: LangChain, Hugging Face, OpenAI

Vector DB: Pinecone

Environment Management: dotenv

📂 Project Structure
Code
End-to-End-Medical-Chat-Bot/
│
├── app.py                # Flask app entry point
├── src/
│   ├── helper.py         # PDF loading, text splitting, embeddings
│   └── prompt.py         # System prompts for chatbot
├── templates/
│   └── chat.html         # Chat UI
├── static/
│   └── style.css         # Styling for chat UI
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
⚙️ Setup
Clone the repo:

bash
git clone https://github.com/yourusername/End-to-End-Medical-Chat-Bot.git
cd End-to-End-Medical-Chat-Bot
Install dependencies:

bash
pip install -r requirements.txt
Add your API keys to .env:

Code
PINECONE_API_KEY=your_pinecone_key
OPENAI_API_KEY=your_openai_key
Run the app:

bash
python app.py
Open in browser:

Code
http://127.0.0.1:8080/
📊 Future Improvements
Add an admin dashboard for analytics and monitoring.

Integrate voice input for hands‑free interaction.

Expand knowledge base with more medical datasets.

Deploy on cloud (Heroku, AWS, or Azure).

⚠️ Disclaimer
This chatbot provides general health information only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
For emergencies, please call your local emergency services.
