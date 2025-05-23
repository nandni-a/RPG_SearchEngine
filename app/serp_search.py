import os
from serpapi import GoogleSearch

SERP_API_KEY = os.getenv("SERP_API_KEY") or "ce639f3b9f7bc841e1b063adf750314b4802c720075059764f67b11e73d263ba"

def search_keyword(keyword, num_results=5):
    params = {
        "engine": "google",
        "q": keyword,
        "api_key": SERP_API_KEY,
        "num": num_results,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    search_results = []
    for res in results.get("organic_results", []):
        title = res.get("title")
        link = res.get("link")
        snippet = res.get("snippet")
        search_results.append({"title": title, "link": link, "snippet": snippet})
    return search_results
