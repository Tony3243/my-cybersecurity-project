# Helper functions (e.g., regex patterns, timestamp parser)
import re

PASSWORD_PATTERN = re.compile(r"(\w{3}\s+\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\s)(Failed password|Accepted password) for ((?:invalid user )?(\w+)) from (\d{1,3}(?:\.\d{1,3}){3}) ")

def extracting_potential_anomaly(line):
    identical = PASSWORD_PATTERN.search(line)
    if identical:
        return identical.groups()
    else:
        return None
