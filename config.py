import os
from dotenv import load_dotenv


def load_api_keys():
    print("Loading environment variables...")
    load_dotenv()

    openai_key = os.getenv("METIS_OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if not openai_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
    if not anthropic_key:
        raise ValueError("ANTHROPIC_API_KEY is not set in the environment variables.")

    return openai_key, anthropic_key


SYSTEM_MESSAGE = (
    "You are an assistant that analyzes the contents of a company website landing page "
    "and creates a short brochure about the company for prospective customers, investors and recruits. "
    "Respond in markdown."
)


METIS_BASE_URL = "https://api.metisai.ir/openai/v1"
