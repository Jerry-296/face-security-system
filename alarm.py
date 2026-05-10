# alarm.py

from database import save_event
from utils import now_str

def trigger_alarm(event_type: str, person_name: str, detail: str):
    """
    告警处理：
    1. 打印告警
    2. 保存到数据库
    """
    time_str = now_str()
    print(f"[ALARM] {time_str} | {event_type} | {person_name} | {detail}")
    save_event(time_str, event_type, person_name, detail)
