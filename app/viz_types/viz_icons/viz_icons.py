from fastapi import APIRouter, Path, Depends, Response
from fastapi.responses import FileResponse
import pathlib
from _middleware.validate_viz_id import validate_viz_id

router: APIRouter = APIRouter()

ICON_PATH: pathlib.Path = pathlib.Path(__file__).parent/"icons"

@router.post("/{id}/sample")
def viz_icons(id:str = Depends(validate_viz_id)) -> FileResponse:
    """
    Retorna les imatges preview de la pestanya Custom Elements
    El nom de la icona ha de coincidir amb la id de la visualització
    """

    file_name = f"{id}.png"

    icon_path: Path = ICON_PATH/file_name

    if not icon_path.exists():
        Response(status_code=404,content="La imatge no existeix")
        return


    return FileResponse(icon_path,media_type="image/png")