import anthropic
from openai import OpenAI
from config import SYSTEM_MESSAGE, METIS_BASE_URL


class LLMService:
    def __init__(self, openai_key, anthropic_key):
        self.openai = OpenAI(api_key=openai_key, base_url=METIS_BASE_URL)
        self.claude = anthropic.Anthropic(api_key=anthropic_key)

    def stream_gpt(self, prompt):
        messages = [
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ]
        stream = self.openai.chat.completions.create(
            model="gpt-4o-mini", messages=messages, stream=True
        )
        result = ""
        for chunk in stream:
            if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content:
                result += chunk.choices[0].delta.content
                yield result

    def stream_claude(self, prompt):
        result = self.claude.messages.stream(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.7,
            system=SYSTEM_MESSAGE,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        response = ""
        with result as stream:
            for text in stream.text_stream:
                response += text or ""
                yield response

    def stream_model(self, prompt, model):
        if model == "GPT":
            yield from self.stream_gpt(prompt)
        elif model == "Claude":
            yield from self.stream_claude(prompt)
        else:
            raise ValueError("Unknown model")