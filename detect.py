import cv2
from ultralytics import YOLO

# 载入 YOLO 模型
model = YOLO("models/yolov8n.pt")
cap = cv2.VideoCapture(1)  # 选择摄像头（OBS 虚拟摄像头）

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
            if conf > 0.5:  # 过滤低置信度
                cls = int(box.cls[0])
                label = model.names[cls]
                detected_objects.append(label)

    return detected_objects
