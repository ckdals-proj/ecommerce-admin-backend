from fastapi import APIRouter, Depends
from typing import Optional

from dependency_injector.wiring import inject, Provide

from app.container import Container

from app.services.module import CategoryService

router = APIRouter(
    prefix="/category",
    tags=['category'],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
@inject
async def read_category(
    name:Optional[str]=None, 
    category_service:CategoryService = Depends(Provide[Container.category_service])):

    if not name:
        return category_service.read_all_name()
    else: 
        return category_service.read_name(name)