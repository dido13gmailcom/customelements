from importlib import import_module

def get_settings(id:str):
    
    #Omplirem l'objecte segons la id sol·licitada
    settings = {
        "regions":[]
    }
    
    #Importació dinàmica per l'objecte settings
    #Aquests objectes es fusionen entre ells i acaben conformant l'objecte settings anterior
    imported_generic = []
    imported_specific = []
    
    #Importem genèrics
    match id:
        
        case s if s.startswith("map_"):
            try:
                
                if id != "map_latlon":
                    imported_generic_module = import_module("render_settings.models.generic.generic_map.generic")
                    imported_generic = imported_generic_module.settings
            except:pass
                
        case _:
            try:
                imported_generic_module = import_module("render_settings.models.generic.generic_chartjs.generic")
                imported_generic = imported_generic_module.settings
            except:pass
                
        
    ##################################################################
        
    #Importem específics
    try:
        imported_specific_module = import_module(f"render_settings.models.templates.{id}")
        imported_specific = imported_specific_module.settings
    except:pass
    
    
    for generic in imported_generic:
        settings["regions"].append(generic)
        
    for specific in imported_specific:
        settings["regions"].append(specific)
    
    #print(settings)
    
    return settings