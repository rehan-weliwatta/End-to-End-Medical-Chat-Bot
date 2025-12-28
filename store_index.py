from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# load environment variables from .env
load_dotenv()

# get Pinecone API key from environment
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medibot"


if index_name not in pc.list_indexes():
    pc.create_index(
        name=index_name,
        dimension=384,  # must match your embedding model output size
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# connect to the index
index = pc.Index(index_name)

# load and split PDF data
extracted_data = load_pdf_file(data=r"F:\End-to-End-Medical-Chat-Bot\Data")
text_chunks = text_split(extracted_data)

# download embeddings
embeddings = download_hugging_face_embeddings()

# store documents in Pinecone
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)
