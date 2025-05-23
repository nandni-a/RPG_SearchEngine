import gradio as gr
from summarizer import summarize_url
from translator import setup_translator_chain
from yt_summarizer import summarize_video, check_link as is_youtube_url
from search_and_scrape import search_and_scrape
from object_detector import detect_objects  

api_key = "AIzaSyDlVCKsmkbHbQHl49zHkzbBbQ7iTRmdBSM"

def handle_query(query, is_keyword):
    components = []

    if is_keyword:
        results = search_and_scrape(query, num_results=5)
        if not results or isinstance(results, str):
            return [f"❌ {results}", gr.update(visible=False)]

        for i, result in enumerate(results, start=1):
            title = result.get("title", f"Result {i}")
            link = result.get("link", "#")
            summary = result.get("summary", "No summary available.")
            components.append(
                f"""
                <div style='border:1px solid #ddd; border-radius:10px; padding:10px; margin-bottom:15px; background:#f9f9f9'>
                <h3>🔗 <a href=\"{link}\" target=\"_blank\">{title}</a></h3>
                <p><strong>📝 Summary:</strong> {summary}</p>
                </div>
                """
            )

    elif is_youtube_url(query):
        summary = summarize_video(query)
        components.append(
            f"""
            <div style='border:1px solid #ddd; border-radius:10px; padding:10px; margin-bottom:15px; background:#fff3cd'>
            <h3>▶️ YouTube Video Summary</h3>
            <p>{summary}</p>
            </div>
            """
        )
    else:
        summary = summarize_url(query, api_key)
        if summary.startswith("Failed to load"):
            return [f"❌ {summary}", gr.update(visible=False)]
        components.append(
            f"""
            <div style='border:1px solid #ddd; border-radius:10px; padding:10px; margin-bottom:15px; background:#e2f0d9'>
            <h3>🌐 Web Page Summary</h3>
            <p>{summary}</p>
            </div>
            """
        )

    combined_html = "\n".join(components)
    return [combined_html, gr.update(visible=True)]

def translate_summary(text, language):
    chain = setup_translator_chain(language)
    return chain.run(text)

def copy_to_clipboard(summary):
    return gr.Textbox.update(value=summary)

def download_summary(summary):
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    return "summary.txt"

# 🚀 Gradio UI
with gr.Blocks(css="""
#header h1 { color: #333; font-weight: bold; font-size: 2.2rem; }
.gr-button {min-width: 130px; background: linear-gradient(to right, #667eea, #764ba2); color: white; border: none; border-radius: 8px;}
.gr-button:hover {opacity: 0.9;}
#footer {text-align: center; color: #666; margin-top: 2em; font-size: 0.9rem;}
""") as demo:

    gr.Markdown("""
    # 🔍 AI Summarizer & Translator

    ### 🌟 Features:
    - 🔑 Search & summarize any topic
    - 🌐 Summarize web pages
    - ▶️ Summarize YouTube videos
    - 🌍 Translate summaries to other languages
    - 📷 Detect objects in images
    - 📃 Copy or download summaries
    """, elem_id="header")

    with gr.Row():
        query_input = gr.Text(label="Enter keyword, website URL, or YouTube link", placeholder="e.g. GPT-4 vs Claude 3 or https://openai.com/")
        keyword_checkbox = gr.Checkbox(label="🔎 Treat as keyword search", value=False)
        generate_btn = gr.Button("Summarize ✨")

    summary_output = gr.HTML(label="📝 Summary", show_label=False)
    translate_btn = gr.Button("Translate 🌍", visible=False)
    lang_dropdown = gr.Dropdown(
        choices=["Hindi", "French", "Spanish", "German", "Arabic", "Chinese"],
        value="Hindi",
        label="Translate to"
    )

    with gr.Row():
        copy_btn = gr.Button("📋 Copy Summary")
        download_btn = gr.Button("📁 Download Summary")

    download_output = gr.File(label="Download link", visible=False)

    generate_btn.click(handle_query, inputs=[query_input, keyword_checkbox], outputs=[summary_output, translate_btn])
    translate_btn.click(translate_summary, inputs=[summary_output, lang_dropdown], outputs=summary_output)
    copy_btn.click(copy_to_clipboard, inputs=summary_output, outputs=query_input)
    download_btn.click(download_summary, inputs=summary_output, outputs=download_output)

    # 📸 Object Detection Section
    gr.Markdown("## 🎯 Object Detection from Image")
    with gr.Row():
        image_input = gr.Image(label="Upload Image", type="filepath")
        detect_btn = gr.Button("Detect Objects 🎯")

    with gr.Column():
        detected_image = gr.Image(label="Detected Image")
        detected_labels = gr.Textbox(label="Detected Objects")

    detect_btn.click(fn=detect_objects, inputs=image_input, outputs=[detected_image, detected_labels])

    gr.Markdown("<div id='footer'>Made with ❤️</div>")

    demo.launch(server_name="0.0.0.0", share=True)
