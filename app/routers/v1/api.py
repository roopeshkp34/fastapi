

from fastapi import APIRouter

from app.routers.v1 import books
from app.routers.v1 import login
from app.routers.v1 import user


router = APIRouter()

router.include_router(books.router, prefix="/books",tags=["Books"])
router.include_router(login.router, prefix="/login",tags=["User"])
router.include_router(user.router, prefix="/user",tags=["User"])
