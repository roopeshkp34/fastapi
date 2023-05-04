from app.crud import CRUDBase
from app import models
from app.schemas.books import BookCreateDB

class CRUDBooks(CRUDBase[models.Books, BookCreateDB, BookCreateDB]):
    pass

books = CRUDBooks(models.Books)