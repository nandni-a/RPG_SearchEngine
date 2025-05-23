import os
from serpapi import GoogleSearch
from summarizer import summarize_url  # Make sure summarizer.py has summarize_url(api_key) function

# SerpAPI key
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "ce639f3b9f7bc841e1b063adf750314b4802c720075059764f67b11e73d263ba")

# Google Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDlVCKsmkbHbQHl49zHkzbBbQ7iTRmdBSM")

def search_and_scrape(keyword, num_results=5):
    params = {
        "engine": "google",
        "q": keyword,
        "api_key": SERPAPI_API_KEY,
        "num": num_results,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "error" in results:
        return f"Error from SerpAPI: {results['error']}"

    pages = []
    for result in results.get("organic_results", []):
        link = result.get("link")
        title = result.get("title", "No Title")

        if link:
            summary = summarize_url(link, GEMINI_API_KEY)
            pages.append({
                "title": title,
                "link": link,
                "summary": summary
            })

        if len(pages) >= num_results:
            break

    if not pages:
        return "No search results found."

    return pages
