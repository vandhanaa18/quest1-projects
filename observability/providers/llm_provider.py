import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()


class ModelProvider:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:

            provider = os.getenv("MODEL_PROVIDER", "groq").lower()

            if provider == "groq":
                cls._model = LiteLlm(
                    model="groq/llama-3.3-70b-versatile",
                    api_key=os.getenv("GROQ_API_KEY"),
                )

            elif provider == "ollama":
                cls._model = LiteLlm(
                    model="ollama_chat/qwen3:8b",
                )

            else:
                raise ValueError(f"Unsupported provider: {provider}")

        return cls._model