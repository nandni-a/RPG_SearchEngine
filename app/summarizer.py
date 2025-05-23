import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader

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

def summarize_url(url, api_key):
    loader = WebBaseLoader(url)
    documents = loader.load()
    if not documents:
        return "Failed to load document."

    text = documents[0].page_content
    prompt_template = PromptTemplate(
        template="""As a professional summarizer, create a detailed and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity.
2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.
3. Rely strictly on the provided text, without including external information.
4. Format the summary in paragraph form for easy understanding.
5. Conclude your notes with [End of Notes, Message #X] to indicate completion, where "X" represents the total number of messages that I have sent.

By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, detailed, and reader-friendly manner. Optimize output as markdown file.

"{text}"

DETAILED SUMMARY:""",
        input_variables=["text"],
    )
    chain = GeminiChain(api_key=api_key, prompt_template=prompt_template)
    summary = chain.run(text)
    return summary
