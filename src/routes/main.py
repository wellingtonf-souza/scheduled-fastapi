from src.config import app
from fastapi import Response, status
import time

@app.get("/")
def healthcheck(response: Response):
    """healthcheck
    """
    response.status_code = status.HTTP_200_OK
    return {"message": "server running"}

@app.get("/sleep")
def sleep(response: Response, secs: int = 10):
    """sleep
    """
    time.sleep(secs)
    response.status_code = status.HTTP_200_OK
    return {"message": "sleep finish"}
