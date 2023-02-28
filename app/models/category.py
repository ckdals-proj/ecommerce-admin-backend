from app.models.base import Base
from app.models.mixin import TimestampMixin

from sqlalchemy import Column, Integer, String

class Category(Base,TimestampMixin):
    name = Column(String(100),index=True,unique=True)
    desc = Column(String(1024))
    picture_path = Column(String(256))