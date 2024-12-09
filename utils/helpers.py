import re

def extract_info_from_line(line):
    regex = r"^(?P<date>\w+ \d+ \d+:\d+:\d+) (?P<host>\S+) (?P<service>\S+): (?P<message>.+)$"
    match = re.match(regex, line)
    if match:
        return match.groupdict()
    return None
