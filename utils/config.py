import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    temperature: float = 0.2  # low for reliability


def get_settings() -> Settings:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment or .env")

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    return Settings(
        openai_api_key=api_key,
        openai_model=model,
    )
