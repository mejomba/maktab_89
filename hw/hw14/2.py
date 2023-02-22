from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


class ServerException(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.status = 500


@app.exception_handler(ServerException)
def server_exception_handler(request: Request, exc: ServerException):
    return JSONResponse(
        content={'message': f'{exc.msg}'},
        status_code=exc.status,
    )


@app.get('/')
def test():
    try:
        # some operation that can be raise exception
        x = 5/0
    except Exception as e:
        # raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='some error...')
        # can send "e" as detail value

        # with custom exception
        raise ServerException('server exception raise')


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)