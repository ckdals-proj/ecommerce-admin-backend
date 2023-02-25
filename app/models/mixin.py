from sqlalchemy import Column,String, DateTime, Boolean
from app.utils.timestamp import service_time

class ByMixin:
    created_by = Column(String)
    updated_by = Column(String)
    
class TimestampMixin:
    created_at = Column(DateTime,default=service_time)
    updated_at = Column(DateTime)

class DeleteMixin:
    deleted_at = Column(DateTime)
    is_deleted = Column(Boolean,default=False)