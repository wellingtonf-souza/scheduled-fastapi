from src.logs import logger
from apscheduler.triggers.interval import IntervalTrigger
import time
from src.jobs.interface import Job

class JobHealthcheck(Job):

    def __init__(
        self, 
        description = 'Healthcheck scheduler', 
        trigger = IntervalTrigger(seconds=10),
        active = True, 
        misfire_grace_time = None
    ):
        self._description = description
        self._trigger = trigger
        self._active = active
        self._misfire_grace_time = misfire_grace_time
    
    def action(self):
        logger.info("scheduler healthcheck running")
