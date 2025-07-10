# main detection logic (read and analyzes logs)
import pandas as pd
import sys
from loguru import logger
from utils import extracting_potential_anomoly

logger.add(sys.stdout, level='WARNING')
logger.add('run.log', level="WARNING")

log_in = 'Scrutinizing file for any possible threats or failed login attempts'
good = 'User has successfully logged in'
sus = 'User is distingusing some abnormal behavior'
failed = 'User surpassed threshold and failed login'


with open('logs/sample_auth.log', 'r') as logs:
    samples = logs.readlines()
    