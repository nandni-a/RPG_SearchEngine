import requests
from bs4 import BeautifulSoup

def scrape_web_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; your-app/1.0)"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Failed to fetch URL: {url}"

        soup = BeautifulSoup(response.text, "html.parser")
        # Simple extraction of all paragraph text
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text() for p in paragraphs)
        if not text.strip():
            return "No meaningful text found at URL."
        return text
    except Exception as e:
        return f"Error scraping URL: {str(e)}"
