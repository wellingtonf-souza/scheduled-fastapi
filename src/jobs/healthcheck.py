from src.logs import logger
from apscheduler.triggers.interval import IntervalTrigger
import time
from src.jobs.interface import Job

class JobHealthcheck(Job):

    def __init__(self):
        super().__init__(
            description = 'Healthcheck scheduler', 
            trigger = IntervalTrigger(seconds=10),
            active = True, 
            misfire_grace_time = None
        )
    
    def action(self):
        logger.info("scheduler healthcheck running")
