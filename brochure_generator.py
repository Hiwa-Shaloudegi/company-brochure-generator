from website_extractor import Website


class BrochureGenerator:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def stream_brochure(self, company_name, url, model):
        prompt = f"Please generate a company brochure for {company_name}. Here is their landing page:\n"
        website = Website(url)
        prompt += website.get_contents()

        yield from self.llm_service.stream_model(prompt, model)
