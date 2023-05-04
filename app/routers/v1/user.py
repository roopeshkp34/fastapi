
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.schemas.user import UserCreate
from app.db.session import get_db

router  = APIRouter()

@router.post("/create")
def create_user(user: UserCreate,db: Session= Depends(get_db)):
    user = crud.user.get_user(db, username=user.username)
    if not user:
        user = crud.user.new(db,user)
    
    return user