# object_detector.py

import torch
from PIL import Image
import numpy as np

# Load YOLOv5s model from ultralytics
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.eval()

def detect_objects(image_path):
    """Detect objects in an image and return annotated image and labels."""
    img = Image.open(image_path).convert("RGB")
    results = model(img)
    results.render()  # updates results.ims with boxes and labels
    output_img = Image.fromarray(results.ims[0])
    labels = results.pandas().xyxy[0]['name'].tolist()
    return output_img, ", ".join(set(labels)) if labels else "No objects detected"
