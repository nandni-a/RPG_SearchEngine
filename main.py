from web_scraper import get_clean_text, summarize
from object_detection import detect_from_camera
from gps_utils import get_plus_code

def run_web_summary():
    print("📡 Fetching and summarizing a webpage...")
    url = "https://en.wikipedia.org/wiki/Augmented_reality"
    text = get_clean_text(url)

    if text:
        print("✅ Text fetched. Generating summary...")
        summary = summarize(text)
        print("\n--- Summary ---\n", summary)
    else:
        print("❌ Failed to fetch or extract content from the URL.")

def run_object_detection():
    print("📷 Starting object detection (webcam)...")
    detect_from_camera()
    print("✅ Object detection should now be visible.")

def run_plus_code_lookup():
    lat, lon = 37.421908, -122.084681
    print(f"🧭 Generating Plus Code for: ({lat}, {lon})")
    plus_code = get_plus_code(lat, lon)
    print("\n--- Plus Code ---\n", plus_code)

if __name__ == "__main__":
    print("🚀 Starting Reality Search Engine...")

    run_web_summary()
    run_object_detection()
    run_plus_code_lookup()

    print("🏁 Program finished.")
