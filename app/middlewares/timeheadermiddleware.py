import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from starlette.types import ASGIApp
import typing

from typing import List

DispatchFunction = typing.Callable[
    [Request, RequestResponseEndpoint], typing.Awaitable[Response]
]


class TimeHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, dispatch: typing.Optional[DispatchFunction] = None, not_allowed_api_list:List=None) -> None:
        super().__init__(app, dispatch)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        res = await call_next(request)
        process_time = time.time() - start_time
        res.headers['X-Process-Time'] = str(process_time)
        print(res,process_time)
        print(res.headers)
        print(request.path_params)
        
        return res