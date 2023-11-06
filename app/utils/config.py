import os
from dotenv import load_dotenv
import weaviate 

load_dotenv('.env') 

WEAVIATE_URL = os.environ.get("WEAVIATE_URL")
WEAVIATE_API_KEY = os.environ.get("WEAVIATE_API_KEY")
HUGGINGFACE_API = os.environ.get("HUGGINGFACE_API_KEY")
BOOKS_URL = os.getenv("BOOKS_URL")


config = {
    "url": WEAVIATE_URL,
    "auth_client_secret": weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    "additional_headers": {
        "X-HuggingFace-Api-Key": HUGGINGFACE_API
    }
}