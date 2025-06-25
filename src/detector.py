# main detection logic (read and analyzes logs)
import pandas as pd
import sys
import re
from loguru import logger

logger.add(sys.stdout, level='WARNING')
logger.add('sample_auth.log', level="WARNING")



with open('logs/sample_auth.log', 'r') as logs:
    samples = logs.readlines()