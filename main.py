from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World@"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import sys
    import uvicorn

    debugging = "pydevd" in sys.modules
    uvicorn.run("main:app", reload=not debugging, host="0.0.0.0", port=8080)
