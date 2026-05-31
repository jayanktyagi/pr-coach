import os
from typing import List, Dict, Optional

from groq import Groq


class GroqClient:
    """
    Thin wrapper around Groq chat completions.
    Keeps LLM concerns isolated from LangGraph / API logic.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "llama-3.3-70b-versatile",
        temperature: float = 0.3,
        max_tokens: int = 1024,
    ):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not set")

        self.client = Groq(api_key=self.api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """
        messages format:
        [
          {"role": "system", "content": "..."},
          {"role": "user", "content": "..."}
        ]
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature or self.temperature,
            max_tokens=max_tokens or self.max_tokens,
        )

        return response.choices[0].message.content.strip()


# ---- singleton-style helper (safe + explicit) ----

_groq_client: Optional[GroqClient] = None


def get_groq_client() -> GroqClient:
    global _groq_client
    if _groq_client is None:
        _groq_client = GroqClient()
    return _groq_client