from detect import detect_objects
from server import send_to_ai
from arduino import send_signal
import time

def main():
    print("od started...")
    
    while True:
        detected_objects = detect_objects()  # 获取物体列表
        print(f"detected objects: {detected_objects}")

        if detected_objects:
            ai_response = send_to_ai(detected_objects)  # 调用 OpenAI
            print(f"ai response: {ai_response}")

            send_signal(True)  # 通知 Arduino
        else:
            send_signal(False)  # 没检测到物体

        time.sleep(1)  # 控制检测间隔，防止过载

if __name__ == "__main__":
    main()
