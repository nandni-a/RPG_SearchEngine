import requests

def google_search(query, api_key):
    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    response.raise_for_status()  # Raise error if something went wrong
    data = response.json()
    
    # Extract URLs from organic search results
    urls = []
    for result in data.get("organic_results", []):
        link = result.get("link")
        if link:
            urls.append(link)
    return urls

if __name__ == "__main__":
    API_KEY = "ce639f3b9f7bc841e1b063adf750314b4802c720075059764f67b11e73d263ba"  # Replace with your actual SerpAPI key
    query = "OpenAI GPT-4"
    urls = google_search(query, API_KEY)
    
    print("Search result URLs:")
    for url in urls:
        print(url)
