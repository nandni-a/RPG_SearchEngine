# Easy Webpage Summarizer

A Python script designed to summarize webpages from specified URLs using the LangChain framework and the ChatOllama model. It leverages advanced language models to generate detailed summaries, making it an invaluable tool for quickly understanding the content of web-based documents.

## Requirements

```bash
pip install -r requirements.txt
```

## Features

- Summarization of webpages and youtube videos directly from URLs.
- Translates to Turkish language (other languages will be added soon!)
- Integration with LangChain and ChatOllama for state-of-the-art summarization.
- Command-line interface for easy use and integration into workflows.

## Usage

To use the webpage summarizer, run the script from the command line, providing the URL of the document you wish to summarize:

```bash
python summarizer.py -u "http://example.com/document"
```

Replace `http://example.com/document` with the actual URL of the document you want to summarize.

### Web UI

To use the webpage summarizer in you web browser, you can also try gradio app.

```bash
python app/webui.py
```

![gradio](assets/gradio.png)

## Docker

```bash
docker build -t web_summarizer .
docker run -p 7860:7860 web_summarizer

# Run if you run ollama on host
docker run -d --network='host' -p 7860:7860 web_summarizer
```

## License

This script is released under the MIT License. See the [LICENSE](./LICENSE) file in the repository for full details.
