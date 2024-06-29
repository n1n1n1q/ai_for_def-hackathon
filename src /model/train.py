"""
Model's training script
"""

from ultralytics import YOLO

model = YOLO("src/model/yolov8n_custom.pt")

model.train(
    data="src/model/data_custom.yaml", batch=8, imgsz=640, epochs=100, workers=1
)
