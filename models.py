from langchain_community.chat_models import ChatOpenAI
from anthropic import Anthropic
from langchain_google_vertexai import ChatVertexAI
from google.cloud import aiplatform
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Load OpenAI GPT model
def load_openai_model():
    """Loads OpenAI's GPT model."""
    return ChatOpenAI(temperature=1.2, model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)

# Load Claude AI model
def load_claude_model():
    """Loads Claude AI model using the Anthropic API."""
    return Anthropic(api_key=CLAUDE_API_KEY)

def load_gemini_model():
    """Loads Gemini model using its API key."""
    aiplatform.init(project="debate-project-445623", location="us-central1")
    return ChatVertexAI(model="gemini-1.5-flash")