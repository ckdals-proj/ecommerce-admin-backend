from fastapi import FastAPI, Depends
from app.controller import admin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)