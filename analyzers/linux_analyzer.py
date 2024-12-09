from models.log_entry import LogEntry

class LinuxAnalyzer:
    def __init__(self, logfile):
        self.logfile = logfile
        self.logs = []

    def run(self):
        with open(self.logfile, "r") as file:
            for line in file:
                log_entry = self.parse_line(line)
                if log_entry:
                    self.logs.append(log_entry)

        self.display_logs()

    def parse_line(self, line):
        # Exemple d'analyse d'une ligne du journal Linux
        parts = line.split()
        if len(parts) > 5:
            timestamp = f"{parts[0]} {parts[1]} {parts[2]}"
            event_type = parts[4]
            message = " ".join(parts[5:])
            return LogEntry(timestamp, event_type, message)
        return None

    def display_logs(self):
        for log in self.logs:
            print(log)
