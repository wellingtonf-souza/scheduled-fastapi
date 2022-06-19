from src.logs import logger
from apscheduler.triggers.cron import CronTrigger
import time
from src.jobs.interface import Job

class JobSaturday(Job):

    def __init__(self):
        super().__init__(
            description = 'Saturday job', 
            trigger = CronTrigger(day_of_week = 'sat', hour = 11, minute = 45, second = 10), 
            active = True,
            misfire_grace_time = None
        )
    
    def action(self):
        logger.info("saturday job running")
