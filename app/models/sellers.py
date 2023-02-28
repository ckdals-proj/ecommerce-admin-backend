from app.models.base import Base
from app.models.mixin import TimestampMixin, DeleteMixin

from sqlalchemy import Column, Integer, String, DateTime

class Sellers(Base, TimestampMixin, DeleteMixin):
    email = Column(String(128),nullable=False, index=True)
    hash_pw = Column(String(256),nullable=False)
    name = Column(String(256))
    tel = Column(String(20))
    phone = Column(String(20))
    address = Column(String(1024))
    postal_code = Column(String(50))

    company_name = Column(String(100))
    company_state = Column(String(100))
    company_address = Column(String(1024))
    company_postal_code = Column(String(50))
    business_code = Column(Integer)
    estb_date = Column(DateTime)
    url = Column(String(256))

    business_reg_no = Column(String(20))
    corporate_reg_no = Column(String(20))
    