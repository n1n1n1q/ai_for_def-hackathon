"""
Object detection model itself
"""

import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("src/model/yolov8n_custom.pt")

cap = cv2.VideoCapture(0)


def get_powerline_position(frame):
    """
    Get the position of the powerline on the frame
    """
    results = model(frame)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = box.cls[0]
            label = model.names[int(cls)]
            if label == "powerline support":
                x1, y1, x2, y2 = box.xyxy[0]
                x_center = int((x1 + x2) / 2)
                y_center = int((y1 + y2) / 2)
                return x_center, y_center
    return None, None
