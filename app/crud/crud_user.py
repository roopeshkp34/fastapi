from typing import Any, Dict
from sqlalchemy.orm import Session

from app.crud import CRUDBase
from app import models
from app.schemas.user import UserCreate
from app.core.hashing import get_hashed_password

class CRUDUsers(CRUDBase[models.User, UserCreate, UserCreate]):
    def get_user(self, db_session: Session, username: str) -> models.User:
        user = db_session.query(models.User).filter(models.User.username == username).first()
        return user
    
    def new(self, db_session: Session, obj_in: UserCreate) -> Dict[str, Any]:
        password = obj_in.dict().pop("password")
        _obj_in = UserCreate(**obj_in.dict())
        _obj_in.password = get_hashed_password(password)

        return super().create(db_session, obj_in=_obj_in)

        


user = CRUDUsers(models.User)