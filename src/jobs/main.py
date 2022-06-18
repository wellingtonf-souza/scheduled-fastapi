from src.logs import logger
from src.config import scheduler
import time
from src.jobs.interface import Job

class Healthcheck(Job):

    def __init__(self, name = 'healthcheck scheduler', trigger='interval', seconds=10, misfire_grace_time = None, hours = None):
        self._name = name
        self._trigger = trigger
        self._seconds = seconds
        self._hours = hours
        self._misfire_grace_time = misfire_grace_time
    
    def action(self):
        logger.info("scheduler healthcheck running")

class Sleep(Job):

    def __init__(self, name = 'healthcheck scheduler', trigger='interval', seconds=20, misfire_grace_time = None, hours = None):
        self._name = name
        self._trigger = trigger
        self._seconds = seconds
        self._hours = hours
        self._misfire_grace_time = misfire_grace_time
    
    def action(self):
        time.sleep(2)
        logger.info("scheduler main running")
