import sqlite3
from config import DB_PATH, TABLE_NAME


with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    print(cursor.fetchone())