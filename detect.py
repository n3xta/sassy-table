import cv2
from ultralytics import YOLO

model = YOLO("models/yolov12n.pt")
cap = cv2.VideoCapture(2)

def detect_objects():
    ret, frame = cap.read()
    if not ret:
        print("摄像头无法获取画面")
        return []

    results = model(frame)
    detected_objects = []

    for result in results:
        for box in result.boxes:
            conf = box.conf[0].item()
            if conf > 0.5:
                cls = int(box.cls[0])
                label = model.names[cls]
                detected_objects.append(label)

    return detected_objects
