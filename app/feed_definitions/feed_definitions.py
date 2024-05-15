from fastapi import APIRouter, Depends
from .models._definitions import get_feed_definitions
from _middleware.validate_viz_id import validate_viz_id


router: APIRouter = APIRouter()

@router.get("/{id}/feeds")
def feed_definitions(id:str = Depends(validate_viz_id)):
    """
    Retorna la definició de la visualització que serà usada pel BO
    en el moment de fer peticions al servidor i renderitzar la gràfica.
    Alguns dels parametres importants són l'obligatorietat dels camps,
    el tipus de dades que agafa, si té 1 o 2 axis, etc...

    La documentació d'aquest apartat pot veure's a:
     <a href='https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/59cf229cf14a426793c56fe0392ac66e/f4317f9d4fb842c89568f826f3e0d1dd.html?locale=en-US' target='_blank'>Documentació BO Feed Definitions</a>
    """

    feed = get_feed_definitions(id)    
    return feed