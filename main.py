from detect import detect_objects
from server import send_to_ai
# from arduino import send_signal
from voice import generate_speech
import time

last_detected_objects = set()
last_ai_response = ""

def main():
    global last_detected_objects, last_ai_response
    print("启动摄像头物体检测...")

    while True:
        detected_objects = set(detect_objects())

        if detected_objects != last_detected_objects:
            print(f"🔍 检测到新物品: {detected_objects}")

            ai_response = send_to_ai(detected_objects)
            print(f"🗣️ AI 生成的内容: {ai_response}")

            if ai_response != last_ai_response:
                generate_speech(ai_response)
                last_ai_response = ai_response

            last_ai_response = ai_response
            # send_signal(bool(detected_objects))

            last_detected_objects = detected_objects

        time.sleep(1)

if __name__ == "__main__":
    main()
