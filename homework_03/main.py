from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> Dict[str, str]:
    return {"message": "My FastAPI application"}


@app.get("/ping/")
def ping() -> Dict[str, str]:
    return {"message": "pong"}
