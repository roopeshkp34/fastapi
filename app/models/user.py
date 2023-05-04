
from datetime import datetime
import sqlalchemy as sa
from app.db.base_class import Base


class User(Base):
    id = sa.Column(sa.Integer(), primary_key=True)
    username = sa.Column(sa.String(255))
    password = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))
    created_on = sa.Column(sa.DateTime, default=datetime.utcnow)
    modified_on = sa.Column(sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = sa.Column(sa.Boolean(), default=True)
