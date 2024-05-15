from render_settings.models.get_settings import get_settings

def get_options(feed,id):
    """
    Les opcions (settings) de les visualitzacions poden venir, o bé via default (carpeta 'render_settings')
    o bé via petició del BO en el feed (solament quan s'ha canviat alguna cosa de l'estat inicial, sinó ve sense res)
    
    Aleshores, segons l'entrada settings del Feed tingui o no dades, aplanem un o altre origen i li donem una 
    estructura comuna (options)
    
    """
    settings = get_settings(id)
    options = parse_default_settings(settings["regions"])

    if len(feed['settings']) > 0:
        options.update(parse_custom_settings(feed))



    return options


def parse_custom_settings(feed):
    """
    Aplana els settings definits en el Feed (només quan l'usuari modifica)
    """
    
    options = {}
    settings = feed['settings']
    
    for setting in settings:
        if "property" in setting and "value" in setting:
            id = setting["property"]
            options[id] = setting["value"]
            

    return options
    
    
    

def parse_default_settings(settings,options={}):
        """
        Aplana l'estructura definida a render_settings 
        """
        
        options = {}
        
        if isinstance(settings, dict):
            if 'id' in settings and 'default' in settings:
                options[settings['id']] = settings['default']
            else:
                for value in settings.values():
                    options.update(parse_default_settings(value))
    
        elif isinstance(settings, list):
            for item in settings:
                options.update(parse_default_settings(item))
            
        
        
        return options



