from fastapi import FastAPI

from app.routers.v1 import api as v1_apis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def index():
    return "Crud APP"

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the domain of your frontend application
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=v1_apis.router, prefix="/v1")