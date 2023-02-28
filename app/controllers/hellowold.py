from fastapi import APIRouter, Depends
from typing import Optional

router = APIRouter(
    tags=['hello world'],
)

@router.get('/')
async def read_category():
    return {'msg':'hello world'}