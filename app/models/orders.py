from app.models.base_class import Base
from app.models.mixin import TimestampMixin, DeleteMixin

from sqlalchemy import Column, Integer, String

class Orders(Base,TimestampMixin):
    buyer_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)

    qty = Column(Integer)
    address = Column(String(1024))
    status = Column(String(128))
    payment_type = Column(String(1024))