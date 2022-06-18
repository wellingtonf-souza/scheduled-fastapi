from src.logs import logger
from src.config import scheduler
import time

def healthcheck()->None:
    """healthcheck scheduler
    """
    logger.info("scheduler healthcheck running")

def sleep()->None:
    """sleep scheduler
    """
    time.sleep(2)
    logger.info("scheduler main running")

scheduler.add_job(func = healthcheck, name = 'healthcheck scheduler', trigger='interval', seconds=10, misfire_grace_time = None)
scheduler.add_job(func = sleep, name = 'main scheduler', trigger='interval', seconds=20, misfire_grace_time = None)
