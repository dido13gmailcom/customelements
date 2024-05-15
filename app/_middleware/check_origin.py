from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from fastapi import Request, Response, Header

class CheckOrigin(BaseHTTPMiddleware):
    
    def __init__(self, app: ASGIApp, white_list: list = []) -> None:
        super().__init__(app)
        self.white_list = white_list
        
    async def dispatch(self, req: Request, call_next):
        
        response: Response = await call_next(req)
        ip = req.client.host
        
        if len(self.white_list) == 0 or ip in self.white_list:
            return response
        
        return Response("<h2>Unauthorized</h2>",status_code=401,media_type="text/html")
            
        
        