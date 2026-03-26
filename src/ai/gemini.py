from typing import Optional

import google.generativeai as genai

from .base import AIPlatform


class Gemini(AIPlatform):
    def __init__(self, api_key: str, system_prompt: Optional[str] = None):
        self.api_key = api_key
        self.system_prompt = system_prompt
        genai.configure(api_key=self.api_key) # type: ignore

        # See more models here: https://ai.google.dev/gemini-api/docs/models
        self.model = genai.GenerativeModel(model_name="gemini-3-flash-preview", # type: ignore
                                           system_instruction=self.system_prompt)

    def refine(self, message: str) -> str:
        response = self.model.generate_content(message); # type: ignore
        return response.text