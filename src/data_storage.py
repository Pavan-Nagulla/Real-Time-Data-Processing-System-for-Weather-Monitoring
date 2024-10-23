# src/data_storage.py

import sqlite3
import os

def init_db():
    """Initialize the database for storing daily weather summaries."""
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/daily_summaries.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            avg_temp REAL NOT NULL,
            max_temp REAL NOT NULL,
            min_temp REAL NOT NULL,
            dominant_condition TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def store_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
    """Store the daily summary in the database."""
    conn = sqlite3.connect('data/daily_summaries.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO daily_summaries (date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, avg_temp, max_temp, min_temp, dominant_condition))

    conn.commit()
    conn.close()
