from ultralytics import YOLO

def detect_from_camera():
    model = YOLO("yolov8n.pt")
    model.predict(source=0, show=True)