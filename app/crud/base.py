


from enum import Enum
from functools import partial
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.base import Base
from app.schemas.search import SkipLimit

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class SaveAction(Enum):
    COMMIT= "COMMIT"
    FLUSH = "FLUSH"
    NONE = "NONE"


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    enum_name_encoder = partial(
        jsonable_encoder, custom_encoder={Enum: lambda x: x.name}
    )
    enum_value_encoder = jsonable_encoder
    def __init__(self, model: Type[ModelType]):
        self.model = model

        self.fields_for_name_encoding = [
            column.name
            for column in self.model.__table__.columns
            if column.type.python_type is not dict
        ]

    def _jsonable_encoder(
        self,
        data: Union[
            Type[ModelType], CreateSchemaType, UpdateSchemaType, Dict[str, Any]
        ],
    ) -> Dict[str, Any]:
        if isinstance(data, self.model):
            data = data.__dict__
        elif not isinstance(data, dict):
            data = data.dict()
        encoded_data = {
            field: (
                CRUDBase.enum_name_encoder(value)
                if field in self.fields_for_name_encoding
                else CRUDBase.enum_value_encoder
            )
            for field, value in data.items()
        }
        return encoded_data
    
    def handle_session(self, db_session: Session, action: SaveAction):
        if action == SaveAction.COMMIT:
            db_session.commit()
        elif action == SaveAction.FLUSH:
            db_session.flush()
        elif action == SaveAction.NONE:
            pass
        else:
            raise NotImplementedError
    
    def get(self, db_session: Session, id: int) -> Optional[ModelType]:
        return db_session.query(self.model).get(id)
    
    def create(
        self,
        db_session: Session,
        obj_in: Union[CreateSchemaType, Dict[str, Any]],
        action: SaveAction = SaveAction.COMMIT
    ) -> Dict[str, object]:
        obj_in_data = self._jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db_session.add(db_obj)
        self.handle_session(db_session, action)
        if action != SaveAction.NONE:
            db_session.refresh(db_obj)
        return db_obj
    
    def update(
        self,
        db_session: Session,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
        refresh_attributes: List[str] = None,
        action: SaveAction = SaveAction.COMMIT
    ) -> Dict[str, object]:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        update_data = self._jsonable_encoder(update_data)
        for field, value in update_data.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        db_session.add(db_obj)
        self.handle_session(db_session, action)
        if action != SaveAction.NONE:
            db_session.refresh(db_obj, attribute_names=refresh_attributes)
        return db_obj
    
    def remove(
        self, db_session: Session, id: int, action: SaveAction = SaveAction.COMMIT
    ) -> ModelType:
        obj = db_session.query(self.model).get(id)
        db_session.delete(obj)
        self.handle_session(db_session, action)
        return obj
    
    def get_multi(
        self, db_session: Session, skip_limit: Optional[SkipLimit] = None
    ) -> List[ModelType]:
        query = db_session.query(self.model)
        if skip_limit:
            query = query.offset(skip_limit.skip).limit(skip_limit.limit)
        return query.all()

