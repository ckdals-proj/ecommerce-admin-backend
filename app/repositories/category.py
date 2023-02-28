from .base import BaseRepository

from app.models.module import Category

from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from sqlalchemy import select

from typing import Dict

class CategoryRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory
    
    def find(self, name):
        with self.session_factory() as session:
            stmt = select(Category).where(Category.name==name)
            category = session.scalars(stmt).first()
            return category

    def findAll(self):
        with self.session_factory() as session:
            stmt = select(Category)
            categorys = session.scalars(stmt).all()
            return categorys