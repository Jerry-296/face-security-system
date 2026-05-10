# app.py

import cv2
from config import APP_NAME, CAMERA_SOURCE
from database import init_db
from recognition import detect_and_recognize
from alarm import trigger_alarm
from utils import now_str

def main():
    print(f"Starting {APP_NAME}...")
    init_db()

    cap = cv2.VideoCapture(CAMERA_SOURCE)

    if not cap.isOpened():
        print("无法打开摄像头或视频源")
        return

    print("按 q 退出程序")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("读取视频流失败")
            break

        result = detect_and_recognize(frame)
        name = result["name"]
        confidence = result["confidence"]

        # 画面显示
        text = f"{name} ({confidence})"
        cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 简单告警逻辑
        if result["is_stranger"]:
            trigger_alarm(
                event_type="STRANGER_DETECTED",
                person_name=name,
                detail=f"检测到陌生人，置信度 {confidence}"
            )

        cv2.imshow(APP_NAME, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[{now_str()}] 程序已退出")

if __name__ == "__main__":
    main()
