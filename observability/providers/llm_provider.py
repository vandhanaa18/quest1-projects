import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()


class ModelProvider:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:

            provider = os.getenv("MODEL_PROVIDER", "ollama").lower()

            if provider == "ollama":
                cls._model = LiteLlm(
                    model=os.getenv("OLLAMA_MODEL"),
                    api_base=os.getenv("OLLAMA_BASE_URL"),
                    num_ctx=131072,
                    reasoning_effort="none",
                )

            elif provider == "groq":
                cls._model = LiteLlm(
                    model="groq/llama-3.1-8b-instant",
                    api_key=os.getenv("GROQ_API_KEY"),
                )

            else:
                raise ValueError(f"Unsupported provider: {provider}")

        return cls._model