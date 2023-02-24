from fastapi import FastAPI, Depends
from app.controller import admin
app = FastAPI()

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
)