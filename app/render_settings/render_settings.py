from fastapi import APIRouter, Depends
from _middleware.validate_viz_id import validate_viz_id
from render_settings.models.get_settings import get_settings
from fastapi import Response
from fastapi.responses import JSONResponse
from traceback import print_exc


router: APIRouter = APIRouter()

@router.get("/{id}/settings")
def render_settings(id:str = Depends(validate_viz_id)) -> Response:
    
    response = Response(status_code=422,content="")
    
    try:
                    
        settings = get_settings(id)
        response = JSONResponse(content=settings)
        
    except Exception as e:
        print_exc()
    
    
    return response