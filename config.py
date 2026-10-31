import os
from pathlib import Path
from dotenv import load_dotenv

# Main project directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from root .env
load_dotenv(BASE_DIR / ".env")

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Project directories
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"

DATABASE_DIR = BASE_DIR / "database"

FAISS_INDEX_DIR = DATABASE_DIR / "faiss_customer_support"

LOGS_DIR = BASE_DIR / "logs"

APP_NAME = "ShopEase AI Customer Support"
APP_VERSION = "1.0.0"

# Create required directories
DATABASE_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)


def validate_configuration():

    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY missing in root .env file.")

    if not KNOWLEDGE_BASE_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge base not found: {KNOWLEDGE_BASE_DIR}"
        )

    files = list(KNOWLEDGE_BASE_DIR.glob("*.md"))

    if not files:
        raise FileNotFoundError("No Markdown policy files found.")

    return True