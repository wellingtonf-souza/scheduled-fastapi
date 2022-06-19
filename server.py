import uvicorn
from src.routes import *
from src.config import app, scheduler
from src.logs import logger
from src.jobs import Job
import json
import warnings
warnings.filterwarnings("ignore")

def load_schedule():
    scheduler.start()
    logger.info("Init Schedule")

def add_jobs():
    jobs = Job.__subclasses__()
    for job in jobs:
        task = job()
        if task.active:
            scheduler.add_job(
                func = task.action, 
                name = task.description, 
                trigger=task.trigger,
                misfire_grace_time = task.misfire_grace_time,
                max_instances=1
            )

@app.on_event("startup")
async def define_status_app():
    json.dump({"running": True},open("status.json", "w"))

@app.on_event("shutdown")
async def shutdown_schedule():
    running = json.load(open("status.json","r"))['running']
    if running:
        json.dump({"running": False},open("status.json", "w"))
        scheduler.shutdown(wait = False)
        logger.info("Shutdown schedule")

if __name__ == '__main__':
    PORT = 3000
    add_jobs()
    load_schedule()
    uvicorn.run(
        "server:app",
        host='0.0.0.0',
        port=PORT,
        reload=False,
        debug=False,
        log_level="info",
        log_config=uvicorn.config.LOGGING_CONFIG
    )
