import folium as fl
import geopandas as gp
import pandas as pd
from pathlib import Path
from render_viz.models.feed_tools.generic.get_options import get_options

class Maps:
    def __init__(self, Feed) -> None:
        self.feed = Feed
        
    def get_html(self):
        
        # DADES
        options = get_options(self.feed.json_feed,self.feed.id) #Opcions -- Settings
        geometries = self.get_geopandas(options) # Capa vectorial
        w,h = self.feed.visualization["options"]["width"], self.feed.visualization["options"]["height"] #Width and Height
        geodata = pd.DataFrame(data={
            "id":self.feed.json_feed['data'][0]['values']['rawvalues'],
            "metric":pd.to_numeric(self.feed.json_feed['data'][1]['values']['rawvalues'],errors="coerce")
        })
        
        is_integer:bool = all([x.is_integer() for x in geodata['metric']])
        if is_integer: 
            geodata["metric"] = geodata["metric"].astype('Int64')
        else:
            geodata["metric"] = geodata["metric"].astype('Float64').round(2)
        
        # Depurem les dades
        geodata = geodata[geodata["id"].isin(geometries["id"].to_list())]
        
        
        title = ""
        if options["show_title"] == "true":
             title = self.feed.json_feed['data'][1]['title']
            
        
        
    
        # Opcions
        bins = int(options["breaks"])
        if bins < 3 or bins > 10: bins = 5
        use_jenks = False      
        
        opacity =  1
        try: opacity = int(options["opacity"])/100 
        except:pass
        if options["opacity"] == 0: opacity = 0
        
       
        
        if  options["method"] == "j":
            use_jenks = True
        
        geometries = geometries.merge(geodata,how="left",on="id")
        geometries = geometries.query("metric.notnull()")
        
        style = """
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

        style = style.replace("font-size:13px",f"font-size:{int(w*0.02)}px")
        style = style.replace("font-size:14px",f"font-size:{int(w*0.025)}px")

        hide_leaflet_logo_script = """
            <style>
                .leaflet-bottom.leaflet-right{
                    display:none !important;
                }
            </style>
        """
        
        
        map = fl.Map(
                    zoom_control=False, 
                    tiles=False, 
                    zoom_start=8,
                    width=w, 
                    height=h,
                    control_scale=True,
                    zoom_snap=0.1)
        
        
        
        try:
            map.get_root().header.add_child(fl.Element(style))
            map.get_root().html.add_child(fl.Element(hide_leaflet_logo_script))

            if len(geometries) > 0:
                distinct_metric_values = len(geometries["metric"].unique())

                ## Thresholds Quantiles
                thrs = None 
                if options["method"] == "q" and distinct_metric_values >= bins:
                    cuts = pd.qcut(geometries["metric"],bins,duplicates="drop")
                    thrs = [x.left for x in sorted(cuts.unique().categories)]
                    thrs.append(geometries["metric"].min())
                    thrs.append(geometries["metric"].max())
                    thrs = sorted(thrs)

                if distinct_metric_values < bins or distinct_metric_values < 3:
                    use_jenks = False

                chr = fl.Choropleth(geometries, 
                            data=geodata,
                            columns=["id","metric"], 
                            key_on="feature.properties.id", 
                            smooth_factor=0, 
                            line_weight=0.5, 
                            line_color="white",
                            fill_color=options["colors"],
                            use_jenks=use_jenks,
                            threshold_scale=thrs,
                            bins = bins,
                            fill_opacity=opacity,
                            legend_name=title,
                            highlight=True,
                            locale = "DE",
                            nan_fill_color="white",
                            nan_fill_opacity=0,
                            nan_line_opacity=0).add_to(map)

                
                
                popup_fields = ["abs_n", "aga_n", "ss_n", "rs_n","metric"]
                popup_aliases = ["ABS: ", "AGA: ","Sector S.: ","Regió: ",f"{self.feed.json_feed['data'][1]['title']}: "]
                
                match self.feed.id:
                    case 'map_rs':
                        popup_fields = ["rs_n","metric"]
                        popup_aliases = ['Regió Sanitària: ',f"{self.feed.json_feed['data'][1]['title']}: "]
                    case 'map_ss':
                        popup_fields = ['ss_n',"rs_n","metric"]
                        popup_aliases = ['Sector Sanitari: ','Regió Sanitària: ',f"{self.feed.json_feed['data'][1]['title']}: "]
                    case 'map_aga':
                        popup_fields = ['aga_n',"rs_n","metric"]
                        popup_aliases = ['AGA: ','Regió Sanitària: ',f"{self.feed.json_feed['data'][1]['title']}: "]
                
                

                fl.GeoJsonPopup(
                    fields=popup_fields,
                    aliases=popup_aliases,
                    localize=True,
                    labels=True,
                    locale = "DE"
                    
                ).add_to(chr.geojson)

                # Borrem llegenda
                for key in chr._children:
                    if key.startswith('color_map'):
                        if options["show_legend"] == "false":
                            del chr._children[key]    
                        else:
                            chr._children[key].width = w/1.8
                    
            if options["tile"] != "false": fl.TileLayer(options["tile"]).add_to(map)
            
            bounds = map.get_bounds()
            try:
                #Una mica de separació entre llegenda i mapa
                if options["show_legend"] != "false":
                    bounds[0][0] = bounds[0][0]+0.1
                    bounds[1][0] = bounds[1][0]+0.1
            except:pass
            map.fit_bounds(bounds,padding=(30,30))
        except:pass
        
        

        pasred_html:str = map.get_root().render()

        obs_range = geometries["metric"].max() - geometries["metric"].min()
        if not is_integer and obs_range < 5:
            pasred_html = pasred_html.replace(
                "d3.svg.axis()",
                r"""d3.svg.axis().tickFormat((value) => d3.format(",.2f")(value).replace(/,/g, 'x').replace(/\./g, ',').replace(/x/g, '.'))"""
                )
        else:
            pasred_html = pasred_html.replace(
                "d3.svg.axis()",
                r"""d3.svg.axis().tickFormat((value) => d3.format(",.0f")(value).replace(/,/g, 'x').replace(/\./g, ',').replace(/x/g, '.'))"""
                )

        return pasred_html

    
    def get_geopandas(self,options):

        id = self.feed.id
        versio = options.get("versio")
        
        if versio == "v" or versio == None:
            versio = ""
        
        geojson_path = Path(__file__).parent.parent/f"geojson/{id}{versio}.geojson"
                
        geopandas = gp.read_file(geojson_path,engine="pyogrio")
        
        return geopandas
                




    


