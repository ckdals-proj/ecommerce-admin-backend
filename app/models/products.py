from app.models.base_class import Base
from sqlalchemy import Column, String, Integer

from app.models.mixin import TimestampMixin, DeleteMixin

class Products(Base, TimestampMixin, DeleteMixin):
    seller_id = Column(Integer,index=True, nullable=False)
    category_id = Column(Integer)

    name = Column(String(50))
    price = Column(Integer)
    qty = Column(Integer)
    desc = Column(String(1024))
    picture_path = Column(String(256))