
from importlib import import_module
from viz_types.models.VIZUALIZATIONS import VisualizationType,VisualizationTypes,visualizations

def get_available_visualizations(visualizations = visualizations, domain = "") -> dict[str,VisualizationType]:
    
    #Comprovem, també, que la visualització tingui un feed_definition associat
    visualizations = get_feed_defined_visualizations(visualizations)
    
    # Si s'especifica un domain, es comprova que la visualització hi pertanyi
    if len(domain) > 0:
        visualizations: VisualizationTypes = VisualizationTypes(
            visualizations= [viz for viz in visualizations.visualizations if viz.domain == domain]
        )

    return visualizations


def get_feed_defined_visualizations(visualizations:VisualizationTypes)->VisualizationTypes:
    """
    Donat un objecte VisualizationTypes, comprova que aquestes visualitzacions tinguin
    associat una definició de feed. Si no en tenen, s'exclouen de la llista ja que
    el BO serà incapaç de processar-ho    
    """

    ids = [viz.id for viz in visualizations.visualizations]
    defined_ids = []
    
    for id in ids:
        try:
            module = import_module(f"feed_definitions.models.tools.{id}")
            if hasattr(module,"definition"):
                defined_ids.append(id)
        except:pass
        
    defined_visualizations: VisualizationTypes = VisualizationTypes(
        visualizations= [viz for viz in visualizations.visualizations if viz.id in defined_ids]
    )
    
    return defined_visualizations
            
        