from fastapi import APIRouter, Request
from .models.viz_types_models import get_available_visualizations, VisualizationTypes

router: APIRouter = APIRouter()

@router.get("/", response_model=VisualizationTypes)
def viz_types(req: Request):
    """
    <p>Retorna el llistat de visualitzacions disponibles.</p>
    <p>Pot veure's l'exemple de dades que BO espera a:</p> <a href='https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/59cf229cf14a426793c56fe0392ac66e/626550266a2f4b2f8a53b5000fa3110a.html?locale=en-US' target='_blank'>Documentació BO</a>
    
    <p>Amb la voluntat de separar millor les diferents visualitzacions, s'afegeix el parametre domain, que permet seccionar el servidor i retornar solament 
    aquelles visualitzacions del domini</p>
    
    <p>Això permet especificar diferents Custom elements al BO i donar-los-hi un nom amb significat dins la galeria</p>    
    """
    
    domain: str = str(req.url).replace(str(req.base_url),"").split("/")[0]

    viz_types: VisualizationTypes = get_available_visualizations(domain=domain)

    return viz_types