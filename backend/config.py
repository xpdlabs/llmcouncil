"""Configuration for the LLM Council."""
import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-5.6-terra-pro",
    "google/gemini-3.5-flash",
    "anthropic/claude-sonnet-5",
    "qwen/qwen3.7-max",
    "x-ai/grok-4.5",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "deepseek/deepseek-v4-pro"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"

# --- Sıcaklık (Temperature) Ayarları ---
COUNCIL_TEMPERATURE = 0.3  # Konsey üyeleri daha net ve rasyonel olsun
CHAIRMAN_TEMPERATURE = 0.1 # Başkan tamamen mantık odaklı olsun ve uydurmasın

# --- Gelişmiş Ayarlar (İsteğe Bağlı) ---
# Destekleyen modeller için akıl yürütme derinliği: "low", "medium", "high"
REASONING_EFFORT = "high"