# recognition.py

import random

def detect_and_recognize(frame):
    """
    原型版识别逻辑：
    这里先返回一个模拟结果，方便你快速搭仓库。
    
    后面你可以替换成：
    - OpenCV 人脸检测
    - InsightFace
    - dlib
    - 其他识别模型
    """
    names = ["Alice", "Bob", "Unknown", "Visitor"]
    name = random.choice(names)
    confidence = round(random.uniform(0.55, 0.99), 2)

    return {
        "name": name,
        "confidence": confidence,
        "is_stranger": name in ["Unknown", "Visitor"]
    }
