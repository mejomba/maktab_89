from fastapi import FastAPI, Form, HTTPException, Body
from pydantic import BaseModel, EmailStr, validator, root_validator, SecretStr
from datetime import datetime
from typing import Optional
import uvicorn
from starlette import status
from starlette.requests import Request
from starlette.templating import Jinja2Templates


app = FastAPI()
template = Jinja2Templates(directory='.')

users = []


class User(BaseModel):
    username: str
    email: EmailStr
    password1: SecretStr
    password2: SecretStr

    @root_validator
    def valid_password1(cls, values):
        if len(values.get('password1')) < 8 or len(values.get('password2')) < 8:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='password must be 8 character')
        elif values.get('password1') != values.get('password2'):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password don't match")
        return values


@app.get('/register')
def user_register(request: Request):
    context = {'request': request}
    return template.TemplateResponse('05.html', context=context)


@app.post('/register')
async def user_register(request: Request):
    """ `users` list can be database table"""

    form = await request.form()

    username = form.get('username')
    email = form.get('email')
    password1 = form.get('password1')
    password2 = form.get('password2')

    try:
        user = User(username=username, email=email, password1=password1, password2=password2)
        users.append(user)
        context = {'request': request, 'user': user}
        return template.TemplateResponse('profile.html', context=context)
    except HTTPException as err:
        context = {'request': request, 'error': err}
        return template.TemplateResponse('profile.html', context=context)


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
