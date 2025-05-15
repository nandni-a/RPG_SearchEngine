import trafilatura
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_clean_text(url):
    """
    Fetch and extract clean text from a URL using trafilatura.
    """
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return None  # Handle invalid or unreachable URLs

    extracted = trafilatura.extract(downloaded)
    return extracted if extracted else None  # Handle non-extractable content

def summarize(text):
    """
    Summarize the input text using a transformer model.
    Automatically truncates the input to avoid token length issues.
    """
    if not text:
        return "No text available to summarize."

    # Approximate limit: 1024 tokens ~ 2000 characters
    if len(text) > 2000:
        text = text[:2000]

    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']
    return result[0]['summary_text']
