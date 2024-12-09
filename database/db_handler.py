import sqlite3

class DBHandler:
    def __init__(self, db_name="logs.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                event_type TEXT,
                message TEXT
            )
        """)
        self.conn.commit()

    def insert_log(self, log_entry):
        self.cursor.execute("INSERT INTO logs (timestamp, event_type, message) VALUES (?, ?, ?)",
                            (log_entry.timestamp, log_entry.event_type, log_entry.message))
        self.conn.commit()

    def fetch_logs(self):
        self.cursor.execute("SELECT * FROM logs")
        return self.cursor.fetchall()
