from src.config import app
from fastapi import Response, status

@app.get("/healthcheck")
def healthcheck(response: Response):
    """healthcheck
    """
    response.status_code = status.HTTP_200_OK
    return {
        "status_code": status.HTTP_200_OK, 
        "message": "success", 
        "data": {
            "message": "server running"
        }
    }

