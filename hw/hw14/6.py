from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional
import uvicorn

app = FastAPI()

users = []


class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    date_joined: Optional[datetime] = datetime.now()

    @validator("password")
    def valid_password(cls, p):
        if len(p) < 8:
            raise ValueError('password must be 8 character')
        return p

    @validator("username")
    def valid_username(cls, u):
        for item in users:
            if u == item.username:
                raise ValueError('username exist')
        return u

    @validator("email")
    def valid_email(cls, e):
        for item in users:
            if e == item.email:
                raise ValueError('email exist')
        return e


@app.post('/')
def test(user: User):
    """ `users` list can be database table"""
    users.append(user)
    return {"data": user}


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)