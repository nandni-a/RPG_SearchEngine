import argparse
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader

import google.generativeai as genai


class GeminiChain:
    def __init__(self, api_key, prompt_template):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.prompt_template = prompt_template
        self.message_count = 0

    def run(self, text):
        self.message_count += 1
        prompt = self.prompt_template.format(text=text)
        prompt += f"\n\n[End of Notes, Message #{self.message_count}]"
        response = self.model.generate_content(prompt)
        return response.text


def setup_argparse():
    """Setup argparse to parse command line arguments."""
    parser = argparse.ArgumentParser(description="Summarize a document from a given URL.")
    parser.add_argument("-u", "--url", required=True, help="URL of the document to summarize")
    return parser.parse_args()


def load_document(url):
    """Load document from the specified URL."""
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents[0].page_content if documents else ""


def setup_summarization_chain(api_key):
    """Setup the summarization chain with Gemini."""
    prompt_template = PromptTemplate(
        template="""As a professional summarizer, create a detailed and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
            1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity.

            2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.

            3. Rely strictly on the provided text, without including external information.

            4. Format the summary in paragraph form for easy understanding.

            5.Conclude your notes with [End of Notes, Message #X] to indicate completion, where "X" represents the total number of messages that I have sent. In other words, include a message counter where you start with #1 and add 1 to the message counter every time I send a message.

        By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, detailed, and reader-friendly manner. Optimize output as markdown file.

        "{text}"

        DETAILED SUMMARY:""",
        input_variables=["text"],
    )
    return GeminiChain(api_key="AIzaSyDlVCKsmkbHbQHl49zHkzbBbQ7iTRmdBSM", prompt_template=prompt_template)


def main():
    args = setup_argparse()
    doc_text = load_document(args.url)
    api_key = "AIzaSyDlVCKsmkbHbQHl49zHkzbBbQ7iTRmdBSM"
    if not doc_text:
        print("Failed to load document.")
        return

    llm_chain = setup_summarization_chain(api_key)
    result = llm_chain.run(doc_text)

    # print("\n--- Summary ---\n")
    # print(result)


if __name__ == "__main__":
    main()
