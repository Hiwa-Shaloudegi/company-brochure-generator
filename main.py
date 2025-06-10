from config import load_api_keys
from llm_service import LLMService
from brochure_generator import BrochureGenerator
from ui import UI


def main():
    """Main application entry point."""
    try:
        openai_key, anthropic_key = load_api_keys()

        llm_service = LLMService(openai_key, anthropic_key)
        brochure_generator = BrochureGenerator(llm_service)

        ui = UI(brochure_generator)
        ui.launch()

    except Exception as e:
        print(f"Error starting application: {e}")
        raise


if __name__ == "__main__":
    main()
