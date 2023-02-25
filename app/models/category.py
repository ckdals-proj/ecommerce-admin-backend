from app.models.base_class import Base
from app.models.mixin import TimestampMixin

from sqlalchemy import Column, Integer, String

class Category(Base,TimestampMixin):
    name = Column(String(100))
    desc = Column(String(1024))
    picture_path = Column(String(256))