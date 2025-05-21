import re
import google.generativeai as genai

from langchain.text_splitter import TokenTextSplitter
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import PromptTemplate
from langchain.schema.document import Document


# Hardcoded Gemini API Key (replace with GitHub Secret)
api_key = "your-gemini-api-key-here"


def check_link(link):
    """Check if the link is a valid YouTube video link."""
    yt_regex = r"^(?:https?:\/\/)?(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]+)(?:\?.*)?$"
    return re.match(yt_regex, link) is not None


def get_transcript(video_link):
    """Fetch transcript from YouTube video."""
    if not check_link(video_link):
        return "Invalid YouTube URL."
    try:
        loader = YoutubeLoader.from_youtube_url(video_link, language=["en", "en-US"])
        transcript = loader.load()
        return transcript
    except Exception as e:
        return f"Failed to retrieve transcript: {e}"


def split_chunks(transcript):
    """Split transcript into token-friendly chunks."""
    splitter = TokenTextSplitter(chunk_size=7500, chunk_overlap=100)
    return splitter.split_documents(transcript)


class GeminiSummarizationChain:
    """Custom chain for summarization using Gemini API."""

    def __init__(self, api_key, prompt_template):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.prompt_template = prompt_template

    def run(self, docs: list[Document]):
        all_summaries = []
        for i, doc in enumerate(docs):
            prompt = self.prompt_template.format(text=doc.page_content)
            try:
                response = self.model.generate_content(prompt)
                result = response.text.strip()
                result += f"\n\n[End of Notes, Message #{i + 1}]"
                all_summaries.append(result)
            except Exception as e:
                all_summaries.append(f"Error during summarization: {e}")
        return "\n\n".join(all_summaries)


def yt_summarization_chain():
    """Create the Gemini-based summarization chain."""
    prompt_template = PromptTemplate(
        template="""As a professional summarizer specialized in video content, create a detailed and comprehensive summary of the YouTube video transcript provided. While crafting your summary, adhere to these guidelines:
            1. Capture the essence of the video, focusing on main ideas and key details. Ensure the summary is in-depth and insightful, reflecting any narrative or instructional elements present in the video.

            2. Exclude any redundant expressions and non-critical details to enhance the clarity and conciseness of the summary.

            3. Base the summary strictly on the transcript provided, avoiding assumptions or additions from external sources.

            4. Present the summary in a well-structured paragraph form, making it easy to read and understand.

            5. Conclude with "[End of Notes, Message #X]", where "X" is the sequence number of the summarizing request, to indicate the completion of the task.

        By adhering to this optimized prompt, you are expected to produce a clear, detailed, and audience-friendly summary that effectively conveys the core content and themes of the YouTube video.

        "{text}"

        DETAILED SUMMARY:""",
        input_variables=["text"],
    )
    return GeminiSummarizationChain(api_key="AIzaSyDlVCKsmkbHbQHl49zHkzbBbQ7iTRmdBSM", prompt_template=prompt_template)


def summarize_video(video_link):
    transcript = get_transcript(video_link)
    if isinstance(transcript, str):
        return transcript  # error string returned

    chunks = split_chunks(transcript)
    sum_chain = yt_summarization_chain()
    result = sum_chain.run(chunks)
    return result
