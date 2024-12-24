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

# Shared settings
GLOBAL_SETTINGS = {
    "temperature": 0.7,        # Default creativity level
    "formality": "neutral",    # Default formality: "neutral", "formal", or "informal"
    "argument_length": "medium"  # Default length: "short", "medium", "long"
}

# Load OpenAI GPT model
def load_openai_model(settings=None):
    """Loads OpenAI's GPT model with customizable settings."""
    if settings is None:
        settings = GLOBAL_SETTINGS
    return ChatOpenAI(
        temperature=settings["temperature"],
        model="gpt-4o-mini",
        openai_api_key=OPENAI_API_KEY
    )

def load_claude_model(settings=None):
    """Loads Claude AI model with customizable settings."""
    if settings is None:
        settings = GLOBAL_SETTINGS
    return Anthropic(api_key=CLAUDE_API_KEY)  # Anthropic-specific configurations are passed at call-time.


def load_gemini_model(settings=None):
    """Loads Gemini model with customizable settings."""
    if settings is None:
        settings = GLOBAL_SETTINGS
    return ChatVertexAI(
        model="gemini-1.5-flash",
        temperature=settings["temperature"]
    )