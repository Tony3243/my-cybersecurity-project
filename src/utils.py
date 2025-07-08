# Helper functions (e.g., regex patterns, timestamp parser)
import re

WRONG_PASSWORD = re.compile(r"Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3}) ")

def extracting_anomoly(line):
    identical = WRONG_PASSWORD.search(line)
    return identical.group(0) if identical else None

CORRECT_PASSWORD = re.compile(r"Accepted password for (\w+) from (\d{1,3}(?:\.\d{1,3}){3}) ")

def extractng_valid_user(line):
    identical = CORRECT_PASSWORD.search(line)
    return identical.group(0) if identical else None
