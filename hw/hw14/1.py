from fastapi import FastAPI
import uvicorn

app = FastAPI()


items = [
    {"id": 1, 'name': 'nokia', 'description': 'nokia the old mobile phone, usually its not expensive'},
    {"id": 2, 'name': 'apple', 'description': 'apple is expensive product'},
    {"id": 3, 'name': 'samsung', 'description': 'samsung smart phone'},
    {"id": 4, 'name': 'xiaomi', 'description': 'xiaomi is a nemidonam'},
]


@app.get('/')
def test(search: str):
    result = []
    for item in items:
        name, description = item.get('name'), item.get('description')
        if search in name or search in description:
            result.append(item)

    return {'data': result}
    # return result


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)