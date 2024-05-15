from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

# Limita la quantitat de dades passades des del BO
class LimitUploadSize(BaseHTTPMiddleware):
    """
    Classe tipus middleware que controla el volum (en bytes) de les peticions
    En el moment d'iniciar-la s'establirà un topall màxim de pes per les request.

    Args:
        max_upload_size (num): topall en bytes de les request passades pel BO
    
    """

    def __init__(self, app: ASGIApp, max_upload_size: float | int) -> None:
        super().__init__(app)
        self.max_upload_size = max_upload_size

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.method == 'POST':
            
            if 'content-length' not in request.headers:
                return Response(status_code=status.HTTP_411_LENGTH_REQUIRED)
            content_length = int(request.headers['content-length'])

            if content_length > self.max_upload_size:
                return Response(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        return await call_next(request)