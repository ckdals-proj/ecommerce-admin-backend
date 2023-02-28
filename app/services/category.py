from fastapi import Depends

from app.repositories.module import CategoryRepository

class CategoryService:
    def __init__(self, category_repository: CategoryRepository) -> None:
        self._repository: CategoryRepository = category_repository

    def read_name(self,name):
        category = self._repository.find(name)
        dto = {"category_name":category.name, "category_desc":category.desc}
        return dto

    def read_all_name(self):
        categorys = self._repository.findAll()
        dto = {"category_list":[{"name":category.name, "desc":category.desc} for category in categorys]}
        return dto