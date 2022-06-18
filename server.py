import uvicorn
from src.routes import *
from src.config import app, scheduler
from src.logs import logger
from src.jobs.interface import Job
from fastapi import Response, status

@app.get("/jobs")
def list_jobs(response: Response):
    """List jobs
    """
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            "job_id": str(job.id), 
            "name": str(job.name), 
            "run_frequency": str(job.trigger), 
            "next_run": str(job.next_run_time)
        })
    response.status_code = status.HTTP_200_OK
    return jobs

def load_schedule():
    scheduler.start()
    logger.info("Init Schedule")

def add_jobs():
    jobs = Job.__subclasses__()
    for job in jobs:
        model = job()
        scheduler.add_job(
            func = model.action, 
            name = model.name, 
            trigger=model.trigger, 
            seconds=model.seconds, 
            misfire_grace_time = model.misfire_grace_time,
            max_instances=1
        )

@app.on_event("shutdown")
async def shutdown_schedule():
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
