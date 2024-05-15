#print(self.headers.get("accept"))

from feed_definitions.models._definitions import get_feed_definitions
from pathlib import Path
from fastapi import BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from html2image import Html2Image
from tempfile import TemporaryDirectory
from viz_types.models.viz_types_models import get_available_visualizations

from render_viz.models.feed_tools.area import Area
from render_viz.models.feed_tools.bars import Bars
from render_viz.models.feed_tools.km import Km
from render_viz.models.feed_tools.lines import Lines
from render_viz.models.feed_tools.maps import Maps
from render_viz.models.feed_tools.mixed import Mixed
from render_viz.models.feed_tools.pyramid import Pyramid
from render_viz.models.feed_tools.sankey import Sankey
from render_viz.models.feed_tools.sunburst import Sunburst
from render_viz.models.feed_tools.map_latlon import MapLatLon
from render_viz.models.feed_tools.not_ready import NotReady

class Feed:
    """
    La classe Feed es nodreix de les dades que el BO passa per
    custom elements, les estructura i les valida i en funció 
    de tot plegat, retorna o bé un HTML o una imatge.

    Args:
        id (str):           id de la visualització segons definició 'feed_definitions'
        json_feed (dict):   rep l'estructura de dades de BO

    Methods:
        -------
    """

    def __init__(self, id:str, json_feed:dict, headers:dict) -> None:
        self.id                 = id            # ID de la gràfica
        self.json_feed          = json_feed     # Dades del BO
        self.headers            = headers       # Headers de la petició
        self.html_templates     = Jinja2Templates(Path(__file__).parent/"html" )                # Directori de les plantilles HTML

        # Dades pròpies
        self.feed_definitions   = get_feed_definitions(id)                                      # Definició del feed (per avaluar)
        self.is_ready           = self._validate_feed()                                         # Disposa la gràfica de tots els elements per a ser renderitzada correctament?    
        self.viz_types          = get_available_visualizations().dict()['visualizations']       # Visualitzacions disponibles (per agafar les descripcions)
        self.visualization      = self.do_visualization()                                      # HTML llest i opcions


    ####################################
    
    def get_custom_element(self, bg_task: BackgroundTasks = None) -> HTMLResponse | FileResponse:

        response = ""
        
        visualization = self.visualization
        html = visualization["html"]
        width, height = visualization["options"]["width"], visualization["options"]["height"]

        if self.headers.get("accept") == "text/html":
            response = HTMLResponse(html)
        
        else:
            with TemporaryDirectory(delete=False,prefix="custom_") as temp_dir:
                temp_path = Path(temp_dir)
                html_parser:Html2Image = Html2Image(output_path=temp_path,
                                                    size=(width,height),
                                                    custom_flags=[
                                                        "--disable-remote-debugging",
                                                        "--disable-gpu",
                                                        "--headless",
                                                        "--disable-bluetooth",
                                                        "--disable-software-rasterizer",
                                                        "--force-device-scale-factor=3"])
                try:
                    html_parser.screenshot(html_str=html,save_as="output.png",size=(width,height))
                except Exception as e:
                    print(f"Error a Feed.get_custom_element:\n {e}")
                
                response = FileResponse(temp_path/"output.png",background=bg_task.add_task(self._remove_temp_directory,temp_path))
                    
        return response        


    def do_visualization(self):
        visualization = {
            "html":"",
            "options":{}
        }
        
        visualization = self.do_options(visualization)
        # Ho reasigno abans perquè necessito les dimensions per fer l'HTML (do_html)
        self.visualization = visualization
        
        visualization = self.do_html(visualization)
        
        return visualization
    
    
    def do_options(self, visualization):
        visualization = self._get_sizes(visualization)
        
        return visualization
    
    
    def do_html(self,visualization):
        
        viz_model = NotReady(self)
        if self.is_ready:
        
            match self.id:
                
                # Bàsics
                case 'lines':
                    viz_model = Lines(self)
                case 'bars':
                    viz_model = Bars(self)
                case 'area':
                    viz_model = Area(self)
                case 'mixed':
                    viz_model = Mixed(self)
                    
                # Analítics
                case 'km':
                    viz_model = Km(self)
                
                # Mapes
                case 'map_latlon':
                    viz_model = MapLatLon(self)
                case s if s.startswith('map_'):
                    viz_model = Maps(self)
            
                
        visualization["html"] = viz_model.get_html()
        
        return visualization
    
    
    
    # Internal methods
    def _validate_feed(self):
        is_ready = False
        is_ready_temp = []
        
        # Definició
        fields = self.feed_definitions['feeds']
        
        try:
            for field in fields:
                
                id = field["id"]
                is_ok= False
                min_requiered = int(field['min']) 

                feed_submitted = [feed for feed in self.json_feed['feeding'] if feed["id"] == id][0]

                if min_requiered> 0:
                    if 'expressions' in feed_submitted.keys():
                        if len(feed_submitted["expressions"]) >= min_requiered:
                            is_ok = True
                elif min_requiered == 0:
                    is_ok = True
                                    
                is_ready_temp.append(is_ok)
                
        except Exception as e:
            print(f"Feed._validate_feed: {e}")      

                

        if all(is_ready_temp):
            is_ready = True


        return is_ready
    

    def _get_sizes(self, visualization):
        
        visualization["options"]["width"] = 400
        visualization["options"]["height"] = 350

        try:

            w = self.json_feed["width"]
            h = self.json_feed["height"]
            dpi = self.json_feed["dpi"]

            s_w = int((w/dpi) * 96)
            s_h = int((h/dpi) * 96)

            visualization["options"]["width"] = s_w 
            visualization["options"]["height"] = s_h
        except Exception as e:
            print(f"Error alhora d'assignar les mides ( Feed._get_sizes() ): \n {e}")


        return visualization
    


    def _remove_temp_directory(self,path:Path) -> None:
        files = path.rglob("*")
        for file in files:
            file.unlink()

        path.rmdir()
    