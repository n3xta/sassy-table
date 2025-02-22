from detect import detect_objects
from server import send_to_ai
from arduino import send_signal
from tts import play_tts
import time

last_detected_objects = set()  # 记录上次检测的物品
last_ai_response = ""  # 记录上次 AI 生成的文本

def main():
    global last_detected_objects, last_ai_response
    print("启动摄像头物体检测...")

    while True:
        detected_objects = set(detect_objects())

        if detected_objects != last_detected_objects:
            print(f"检测到新物品: {detected_objects}")

            if detected_objects:
                prompt = f"桌上有{', '.join(detected_objects)}，请用有趣的方式描述这场景。"
            else:
                prompt = "桌子现在是空的，你可以说点有趣的内容。"

            ai_response = send_to_ai(prompt)  # 发送给 AI，获取生成的文本
            print(f"AI 生成的内容: {ai_response}")

            # 只有当 AI 响应发生变化时才播报
            if ai_response != last_ai_response:
                play_tts(ai_response)  # 播放 TTS 语音
                last_ai_response = ai_response

            send_signal(bool(detected_objects))

            last_detected_objects = detected_objects  # 更新记录

        time.sleep(1)  # 控制检测间隔，防止 CPU 过载

if __name__ == "__main__":
    main()
