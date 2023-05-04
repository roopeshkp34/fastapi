from sqlalchemy.orm import Session

from app import crud
from app.core.hashing import verify_password


def authenticate_user(db: Session, username: str, password: str):
    user = crud.user.get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user