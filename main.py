from fastapi import FastAPI

from app.routers.v1 import api as v1_apis

app = FastAPI()

@app.get("/")
def index():
    return "Crud APP"

app.include_router(router=v1_apis.router, prefix="/v1")