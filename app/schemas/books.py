

from datetime import datetime
from typing import List
from pydantic import BaseModel
from app.schemas.base import BaseResponse

class BookBase(BaseModel):
    title: str
    author: str
    created_on: datetime
    modified_on: datetime
    is_active: bool

class BookResponse(BookBase):
    id: int
    class Config:
        orm_mode = True

class BookCreateBase(BaseModel):
    title: str
    author: str

class BookCreateDB(BookCreateBase):
    user: int
    
class Book(BaseResponse):
    result: List[BookResponse]