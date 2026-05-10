# config.py

APP_NAME = "Face Security System"
CAMERA_SOURCE = 0  # 0 表示默认摄像头，也可以写视频文件路径或 RTSP 地址
LOG_DIR = "data/logs"

# 告警阈值
ALARM_COOLDOWN_SECONDS = 10

# 示例名单
WHITE_LIST = ["Alice", "Bob"]
BLACK_LIST = ["Unknown-Black-1", "Unknown-Black-2"]
