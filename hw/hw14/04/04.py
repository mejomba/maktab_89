from fastapi import FastAPI
import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates

template = Jinja2Templates(directory='.')

app = FastAPI()


data = [
           {'item': 'movie', 'rating': 1},
           {'item': 'movie', 'rating': 2},
           {'item': 'movie', 'rating': 3},
]


@app.get('/list/')
def test(request: Request, reverse: bool = True):
    """ `items` can select from database"""
    items = [
        {"item": "mobile", "name": 'Apple iphone 12', "price": 800},
        {"item": "laptop", "name": 'lenovo gaming', "price": 1700},
        {"item": "car", "name": 'nisan GTR 2020', "price": 145000},
    ]

    context = {"request": request, "items": items, "reverse": reverse}
    return template.TemplateResponse('04.html', context=context)


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app")