import requests
from bs4 import BeautifulSoup


class Website:
    """A class to represent and extract content from a webpage."""

    def __init__(self, url):
        self.url = url
        self._extract_content()

    def _extract_content(self):
        response = requests.get(self.url)
        self.body = response.content
        soup = BeautifulSoup(self.body, "html.parser")

        # Extract title
        self.title = soup.title.string if soup.title else "No title found"

        # Remove irrelevant elements
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()

        # Extract text content
        self.text = soup.body.get_text(separator="\n", strip=True)

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"
