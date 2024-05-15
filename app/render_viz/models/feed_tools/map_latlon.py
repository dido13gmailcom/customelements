import folium as fl
from render_viz.models.feed_tools.generic.get_options import get_options
from jinja2 import Template
import polars as pl

class MapLatLon:
    def __init__(self, Feed) -> None:
        self.feed = Feed
        self.style = """
                <style>
                    div:first-of-type{background-color:white}
                    .leaflet-control-attribution{display:none}
                    .caption{
                        font-weight:bold;
                        font-size:14px;
                        transform:translateY(10px);
                        background-color:transparent !important
                    }
                    #legend{
                        min-height:500px;
                        background-color:transparent !important
                    }
                    .leaflet-top.leaflet-right > div:first-child {
                        background-color:transparent !important
                    }
                    .tick > text{
                        font-size:13px
                    }
                    .leaflet-control-scale{
                        display:none
                    }
                </style>
                """
        self.style_layer_control = """
                    <style>
                    
                        .leaflet-control-layers-selector{
                            margin: 0 !important;
                        }
                    
                        .leaflet-control-layers-overlays{
                            padding: 1rem;
                        }
                    
                        .leaflet-control-layers-overlays > label > span{
                            display:grid;
                            grid-template-columns: 20px minmax(100px,auto);
                            grid-template-rows: auto;
                            column-gap: 1rem;
                            align-items: stretch;
                            margin: auto 0;
                        }
                        
                        .custom-control{
                            display:grid;
                            width:100%;
                            grid-template-columns: minmax(100px,auto) 50px;
                            column-gap: 1rem;
                            align-items:center;
                            margin: 0.3rem;
                        }
                        
                        .custom-icon{
                            margin:auto auto
                        }
                    
                    </style>
                """
        self.style_template = Template(
                """
                {% macro script(this,kwargs) %}
                    var {{ this.get_name() }}_layers = {
                        overlays :  {
                            {%- for key, val in this.overlays.items() %}
                            {{ key|tojson }} : {{val}},
                            {%- endfor %}
                        },
                    };
                    let {{ this.get_name() }} = L.control.layers(
                        {{ this.get_name() }}_layers.base_layers,
                        {{ this.get_name() }}_layers.overlays,
                        {{ this.options|tojson }}
                    ).addTo({{this._parent.get_name()}});

                {% endmacro %}
                
                """
            )
        self.has_legend = False
        self.has_popups = False
        
    def get_html(self):
        
        # Estils i mesures
        w,h = self.feed.visualization["options"]["width"], self.feed.visualization["options"]["height"]
        fl.LayerControl._template = self.style_template 
        default_marker_color = "#74C0FC"
        icon_size = self.__get_icon_size()
        
        # Les opcions
        options = get_options(self.feed.json_feed,self.feed.id) #Opcions -- Settings
        print(options)
        
        # Iniciem el mapa
        map = fl.Map(tiles=options["tile"],width=w,height=h,zoom_snap=0.1,zoom_control=False)
        
        # Comencem (si falla es retorna el mapa sense dades)
        try:
            
            data = self.__parse_dataframe()

            if self.has_legend: self.__add_legend_to(map) #TODO
            if self.has_popups: self.__add_popups_to(map) #TODO
            
            
            # Últims retocs
            map.fit_bounds(map.get_bounds(),padding=(30,30))
            map.get_root().header.add_child(fl.Element(self.style))
            map.get_root().html.add_child(fl.Element(self.style_layer_control))
        except Exception as e:
            print(f"Error a map_latlon: \n {e}")



        return map.get_root().render()
    
    def get_options(self):
        return None
    
    
    def __get_icon_size(self) -> int:
        
        icon_size = 30
        w = self.feed.visualization["options"]["width"]

        match w:
            case _ if w <= 450:
                icon_size = 10
            case _ if w <= 500:
                icon_size = 15
            case _ if w <= 600:
                icon_size = 20
                
        return icon_size
    
    def __parse_dataframe(self) -> pl.DataFrame:

        data: pl.DataFrame = pl.DataFrame()
        
        raw_data:dict = self.feed.json_feed["data"]
        feedings:dict = self.feed.json_feed["feeding"]

        geo_feedings:dict = {}
        legend_feedings:dict = {}
        for feed in feedings:
            if feed["id"] == "geo":
                geo_feedings = feed 
            elif feed["id"] == "legend":
                legend_feedings = feed

        geo_expressions     = geo_feedings.get("expressions")
        legend_expression  = legend_feedings.get("expressions")

        if len(geo_expressions) > 2:    self.has_popups = True 
        if legend_expression:          self.has_legend = True

        for i,ids in enumerate(geo_expressions):
            id_expression = int(ids.get("dataId"))
            data_list = []
            name = ""

            for data_feed in raw_data:
                
                if int(data_feed["id"]) == id_expression:
                    data_list = data_feed["values"]["rawvalues"]
                    name = data_feed["title"]
                    break 

            if i == 0:
                data = data.with_columns(
                    pl.Series(name="lat",values=data_list,dtype=pl.Float64, strict=False)
                )
                continue
            if i == 1:
                data = data.with_columns(
                    pl.Series(name="lon",values=data_list,dtype=pl.Float64, strict=False)
                )
                continue
            
            # Popups
            data = data.with_columns(
                pl.Series(name=name, values=data_list, dtype = pl.Utf8)
            )

        if self.has_legend:
            legend_id = int(legend_expression[0]["dataId"])
            for data_feed in raw_data:
                if int(data_feed["id"]) == legend_id:
                    data_list = map(str,data_feed["values"]["rawvalues"])
                    name = data_feed["title"]

                    data = data.with_columns(
                        pl.Series(name=name, values=data_list, dtype = pl.Utf8)
                    )

        data = data.fill_nan(None).drop_nulls()

        return data

        def __add_legend_to(self,map):
            pass

        def __add_popups_to(self,map):
            pass

        