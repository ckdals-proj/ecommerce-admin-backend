from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.module import routers
from app.container import Container

from app.middlewares.module import TimeHeaderMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

def create_app() -> FastAPI:
    container = Container()
    container.wire(packages=["app.controllers"])

    app = FastAPI()

    for router in routers: 
        app.include_router(router, prefix='/api/v1')

    app.add_middleware(
        TimeHeaderMiddleware, not_allowed_api_list=['/docs']
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app =  create_app()