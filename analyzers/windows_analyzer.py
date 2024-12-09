import win32evtlog
from models.log_entry import LogEntry

class WindowsAnalyzer:
    def __init__(self):
        self.logs = []

    def run(self):
        server = 'localhost'
        log_type = 'Security'
        handle = win32evtlog.OpenEventLog(server, log_type)

        events = win32evtlog.ReadEventLog(handle, win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_FORWARDS_READ, 0)
        for event in events:
            log_entry = LogEntry(event.TimeGenerated, event.SourceName, event.EventID)
            self.logs.append(log_entry)

        self.display_logs()

    def display_logs(self):
        for log in self.logs:
            print(log)
