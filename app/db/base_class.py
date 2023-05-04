from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base, declared_attr


def snake_case(cam_case: str) -> str:
    return "".join(["_" + c.lower() if c.isupper() else c for c in cam_case]).lstrip("_")

class CustomBase(object):
    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)
    
meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
        }
)

Base = declarative_base(cls=CustomBase, metadata=meta)