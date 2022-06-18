from src.config import app
from fastapi import Response, status
import time

@app.get("/sleep")
def sleep(response: Response, secs: int = 10):
    """sleep
    """
    time.sleep(secs)
    response.status_code = status.HTTP_200_OK
    return {
        "status_code": status.HTTP_200_OK, 
        "message": "success", 
        "data": {
            "message": "sleep finish"
        }
    }