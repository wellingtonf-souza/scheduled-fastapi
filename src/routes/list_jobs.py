from src.config import app, scheduler
from fastapi import Response, status

@app.get("/jobs")
def list_jobs(response: Response):
    """List jobs
    """
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            "job_id": str(job.id), 
            "description": str(job.name), 
            "run_frequency": str(job.trigger), 
            "next_run": str(job.next_run_time)
        })
    response.status_code = status.HTTP_200_OK
    return jobs