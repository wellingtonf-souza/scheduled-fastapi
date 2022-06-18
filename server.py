import uvicorn
from src.routes import *
from src.config import app, scheduler
from src.logs import logger
from src.jobs import *

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

@app.on_event("shutdown")
async def shutdown_schedule():
    scheduler.shutdown(wait = False)
    logger.info("Shutdown schedule")

if __name__ == '__main__':
    PORT = 3000
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
