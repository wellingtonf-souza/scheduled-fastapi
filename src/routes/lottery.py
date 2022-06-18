from src.config import app
from fastapi import Response, status
import random

@app.get("/lottery")
def lottery(response: Response):
    """lottery
    """
    numbers = random.sample(range(1,60,1), k = 6)
    response.status_code = status.HTTP_200_OK
    return {
        "status_code": status.HTTP_200_OK, 
        "message": "success", 
        "data": {
            "message": "lottery numbers drawn",
            "numbers": numbers
        }
    }