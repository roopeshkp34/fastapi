
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.routers.v1.utils.user import get_current_user
from app.schemas.user import User, UserCreate
from app.db.session import get_db

router  = APIRouter()

@router.post("/create")
def create_user(user: UserCreate,db: Session= Depends(get_db)):
    user = crud.user.get_user(db, username=user.username)
    if not user:
        user = crud.user.new(db,user)
    
    return user

@router.get("/me", response_model=User)
def me(db: Session = Depends(get_db), current_user = Depends(get_current_user)) -> User:
    
    
    return current_user