from web_scraper import get_clean_text, summarize
from object_detection import detect_from_camera
from gps_utils import get_plus_code

def run_web_summary():
    url = "https://en.wikipedia.org/wiki/Augmented_reality"
    print(f"\nFetching and summarizing: {url}")
    text = get_clean_text(url)

    if text:
        summary = summarize(text)
        print("\n--- Summary ---\n", summary)
    else:
        print("❌ Failed to fetch or extract content from the URL.")

def run_object_detection():
    print("\nStarting object detection from webcam...")
    try:
        detect_from_camera()
    except Exception as e:
        print(f"❌ Error during object detection: {e}")

def run_plus_code_lookup():
    lat, lon = 37.421908, -122.084681
    print(f"\nGenerating Plus Code for location: ({lat}, {lon})")
    try:
        plus_code = get_plus_code(lat, lon)
        print("\n--- Plus Code ---\n", plus_code)
    except Exception as e:
        print(f"❌ Error getting Plus Code: {e}")

if __name__ == "__main__":
    run_web_summary()
    run_object_detection()
    run_plus_code_lookup()
