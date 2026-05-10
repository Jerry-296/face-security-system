# Face Security System

基于 Python + OpenCV 的人脸识别安防系统原型，用于实现视频流接入、人员识别、黑白名单比对、异常告警和日志记录等功能。

## 项目简介

本项目用于验证 AI/视觉识别在安防场景中的应用能力，支持：
- 视频流输入
- 人脸检测与识别
- 黑白名单管理
- 异常事件告警
- 识别日志记录

## 技术栈

- Python 3.10+
- OpenCV
- NumPy
- SQLite
- （可选）Gemini 2 用于告警摘要与事件解释

## 目录结构

```text
face-security-system/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── utils.py
├── alarm.py
├── database.py
├── recognition.py
└── data/logs/
