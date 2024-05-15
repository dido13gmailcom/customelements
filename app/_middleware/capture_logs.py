from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from fastapi import Request, Response, Header
from starlette.types import ASGIApp


class CaptureLogs(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, req: Request,call_next):
        response: Response = await call_next(req)

        return response
    