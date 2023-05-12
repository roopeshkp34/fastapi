
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr


class User(BaseModel): 
    username: str
    email: EmailStr
    id: int

    class Config:
        orm_mode = True