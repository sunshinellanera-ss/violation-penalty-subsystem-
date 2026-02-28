import sqlite3

DATABASE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS violations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student TEXT NOT NULL,
            course TEXT NOT NULL,
            year TEXT NOT NULL,
            violation_type TEXT NOT NULL,
            offense_count INTEGER NOT NULL,
            penalty TEXT NOT NULL,
            status TEXT NOT NULL,
            officer TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()