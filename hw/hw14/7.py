from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request

app = FastAPI()


class Data(BaseModel):
    data: List[int]


@app.post('/')
def test(payload: Data):
    sum_ = 0
    for number in payload.data:
        if number % 2 == 0:
            sum_ += number
    return [sum_]
    # return {"data": [sum_]}


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)

    """sample data for test in postman"""
    # {
    #     "data": [2, 24, 51, 6, 4, "12"]
    # }
