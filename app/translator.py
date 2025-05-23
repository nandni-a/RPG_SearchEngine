from langchain.prompts import PromptTemplate
import google.generativeai as genai

# Set your Gemini API key here (replace with GitHub Secrets later)
api_key = "AIzaSyDlVCKsmkbHbQHl49zHkzbBbQ7iTRmdBSM"


class GeminiTranslatorChain:
    def __init__(self, api_key, prompt_template, target_language):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.prompt_template = prompt_template
        self.target_language = target_language

    def run(self, text):
        prompt = self.prompt_template.format(text=text, language=self.target_language)
        response = self.model.generate_content(prompt)
        return response.text


def setup_translator_chain(language):
    """Setup the translation chain using Gemini API."""
    prompt_template = PromptTemplate(
        template="""As a professional translator, provide a detailed and comprehensive translation of the provided text into "{language}", ensuring that the translation is accurate, coherent, and faithful to the original text.

        "{text}"

        DETAILED TRANSLATION:""",
        input_variables=["text", "language"],
    )

    return GeminiTranslatorChain(api_key=api_key, prompt_template=prompt_template, target_language=language)

import argparse

def main():
    parser = argparse.ArgumentParser(description="Translate text using Gemini API.")
    parser.add_argument("-t", "--text", required=True, help="Text to translate")
    parser.add_argument("-l", "--language", required=True, help="Target language (e.g., Hindi, French)")
    args = parser.parse_args()

    translator = setup_translator_chain(args.language)
    result = translator.run(args.text)

    print("\n--- Translation ---\n")
    print(result)

if __name__ == "__main__":
    main()
