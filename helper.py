import cv2

def check_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"摄像头索引 {index} 无法打开")
        return

    print(f"打开摄像头索引 {index}，按 'q' 退出")
    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"摄像头索引 {index} 没有捕获到画面")
            break

        cv2.imshow(f"摄像头 {index}", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


check_camera(2)
