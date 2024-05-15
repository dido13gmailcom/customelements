from pydantic import BaseModel
class VisualizationType(BaseModel):
    id: str
    name: str
    description: str
    info: str = ""
    domain: str = ""

class VisualizationTypes(BaseModel):
    visualizations: list[VisualizationType]


############################################################################################################################
visualizations: VisualizationTypes = VisualizationTypes(
        visualizations= [

            #Mapes
            VisualizationType(id="map_abs",
                              name="Mapa d'ABS",
                              description="Mapa a nivell d'ABS", 
                              domain="maps",
                              info=""),
            VisualizationType(id="map_aga",
                              name="Mapa d'AGA",
                              description="Mapa a nivell d'AGA", 
                              domain="maps", 
                              info="Es permet escollir diferents versions del mapa. Utilitzeu el codi de l'entitat versionat o vigent segons toqui."),
            VisualizationType(id="map_ss",
                              name="Mapa Sectors Sanitaris",
                              description="Mapa a nivell de Sectors Sanitaris", 
                              domain="maps",
                              info="Es permet escollir diferents versions del mapa. Utilitzeu el codi de l'entitat versionat o vigent segons toqui."),
            VisualizationType(id="map_rs",
                              name="Mapa de Regions Sanitàries",
                              description="Mapa a nivell de Regions Sanitàries", 
                              domain="maps",
                              info="Es permet escollir diferents versions del mapa. Utilitzeu el codi de l'entitat versionat o vigent segons toqui."),
            VisualizationType(id="map_latlon",
                              name="Mapa de latitud i longitud",
                              description="Mapa de marcadors georeferenciats", 
                              info ="Respecteu l'ordre de les variables obligatòries latitud i longitud; es permet fins a un màxim de 6 dimensions més, el valor de les quals apareixeran com a popup al clicar sobre el marcador.",
                              domain="maps")
        ]
    )
############################################################################################################################









    
    