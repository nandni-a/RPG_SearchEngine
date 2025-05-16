# 🧠 Reality Search Engine – Phase 1: Step 1

## 🌐 Web Page Summarization | 📷 Object Detection | 📍 GPS Plus Code

This module is the first working version of the **Reality Search Engine**, combining basic summarization, object recognition, and location tagging.

---

## ✅ Features

* ✅ **Summarizes any web page** using Hugging Face’s BART model (`facebook/bart-large-cnn`)
* ✅ **Detects real-world objects** in real-time via webcam (YOLOv8)
* ✅ **Generates a Plus Code** from given GPS coordinates

---

## 📁 Project Structure

```
RPG_SearchEngine/
├── main.py              # Entry point to run all features
├── web_scraper.py       # Fetch + summarize web content
├── object_detection.py  # Real-time object detection using webcam
├── gps_utils.py         # Plus Code generation from lat/lon
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/RPG_SearchEngine.git
cd RPG_SearchEngine
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install transformers trafilatura ultralytics openlocationcode
pip install torch torchvision torchaudio  # If not already installed
pip install opencv-python
```

---

## 🚀 Run the Project

```bash
python main.py
```

---

## 📋 What You'll See

1. **Web Page Summarization**

   * Fetches a predefined URL (e.g., Wikipedia)
   * Outputs a clean summary

2. **Webcam Object Detection**

   * Opens your webcam
   * Detects and labels objects in real-time

3. **Plus Code Generation**

   * Generates a Plus Code from sample coordinates

---

## 📍 Example Output

```
--- Summary ---
Augmented reality (AR) is the overlaying of digital content on the real world...

--- Object Detection ---
(Press 'q' to close the webcam window)

--- Plus Code ---
849VCWC8+Q9
```

---

## 🧠 Next Steps

Proceed to **Phase 1 – Step 2** to:

* Map the environment in 3D
* Associate digital content with physical coordinates
