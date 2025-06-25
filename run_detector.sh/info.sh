#!/bin/bash

LOG_FILE="logs/auth_sample.log"
THRESHOLD=5

echo "Running Cyber Threat Detector..."
python3 src/detector.py --log_file "$LOG_FILE" --threshold "$THRESHOLD"