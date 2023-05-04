

from datetime import datetime
from pydantic import BaseModel

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
    