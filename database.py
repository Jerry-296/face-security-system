# database.py

import sqlite3
from pathlib import Path
from config import LOG_DIR
from utils import ensure_dir

DB_PATH = Path(LOG_DIR) / "events.db"

def init_db():
    ensure_dir(LOG_DIR)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_time TEXT,
            event_type TEXT,
            person_name TEXT,
            detail TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_event(event_time, event_type, person_name, detail):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO events (event_time, event_type, person_name, detail)
        VALUES (?, ?, ?, ?)
    """, (event_time, event_type, person_name, detail))
    conn.commit()
    conn.close()

def list_events(limit=20):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT event_time, event_type, person_name, detail
        FROM events
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
