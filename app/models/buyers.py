from app.models.base_class import Base
from app.models.mixin import TimestampMixin, DeleteMixin

from sqlalchemy import Column, Integer, String

class Buyers(Base, TimestampMixin, DeleteMixin):
    email = Column(String(128),nullable=False, index=True)
    hash_pw = Column(String(256),nullable=False)
    name = Column(String(256))
    tel = Column(String(128))
    phone = Column(String(20))
    address = Column(String(1024))
    postal_code = Column(String(50))