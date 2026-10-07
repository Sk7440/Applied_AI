from ultralytics import YOLO

# Load model (replace with yolov8n.pt or yolo11n.pt if not custom)
model = YOLO("yolo26n.pt")

# Run real-time inference on webcam
model.predict(source=0, show=True)