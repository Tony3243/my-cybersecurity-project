# Helper functions (e.g., regex patterns, timestamp parser)
import re

PASSWORD_PATTERN = re.compile(r"\w{3}\s+\d{1,2}\s\d{2,1}:\d{2,1}:\d{2,1}\s(Failed password|Accepted password) for (?:invalid user )?(\w+)(\d{1,3}(?:\.\d{1,3}){3}) ")

def extracting_potential_anomoly(line):
    identical = PASSWORD_PATTERN.search(line)
    groups = identical.groups(1,2,3,4)
    if all(groups):
        print("Time Stamp: ", groups[0])
        print("Activity: ", groups[1])
        print("User: ", groups[2])
        print("IP Address: ", groups[3])
    else:
        return None
