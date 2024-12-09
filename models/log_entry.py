class LogEntry:
    def __init__(self, timestamp, event_type, message):
        self.timestamp = timestamp
        self.event_type = event_type
        self.message = message

    def __str__(self):
        return f"[{self.timestamp}] {self.event_type}: {self.message}"
