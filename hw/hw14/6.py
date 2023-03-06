from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request

app = FastAPI()


class Data(BaseModel):
    data: List


@app.post('/totalprice')
def test(request: Request, payload: Data):
    if request.headers.get('Content-Type').lower() == 'application/json':
        sum_ = 0
        for item in payload.data:
            sum_ += item['price']
        return {'sum': sum_}
    else:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='request not a json')


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app")

    """sample data for test in postman"""
    # {"data": [
    #     {"item1": "mobile", "price": 5000},
    #     {"item2": "laptop", "price": 15000},
    #     {"item3": "car", "price": 45000},
    #     {"item4": "home", "price": 245000}
    #     ]
    # }
