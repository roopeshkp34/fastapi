

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app import crud
from app.db.session import get_db
from app.schemas.books import BookCreateDB, BookResponse, BookCreateBase, Book
from app.routers.v1.utils.user import get_current_user

router = APIRouter()

@router.get("/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db), current_user = Depends(get_current_user)) -> List[BookResponse]:
    return crud.books.get_multi(db_session=db)

@router.post("/", response_model=BookResponse)
def create_books(book: BookCreateBase, db: Session = Depends(get_db), current_user = Depends(get_current_user))-> BookResponse:
    obj_in = BookCreateDB(**book.dict(), user=current_user.id)
    return crud.books.create(db, obj_in)

@router.get("/book", response_model=Book)
def get_books(db: Session = Depends(get_db)) -> Book:
    try:
        return Book(message="Success", result=crud.books.get_multi(db_session=db))
    except:
        raise HTTPException(detail="message", status_code=status.HTTP_400_BAD_REQUEST)