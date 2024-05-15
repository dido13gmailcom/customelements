## La definició d'un feed es basa en un array dins la clau feed.
## Cada entrada pot prendre el valor de mesura o dimensió i pot ser opcional, obligatori.
## Tot plegat s'acaba traduint en l'agregació clàssica: dimensions --> group by, mesures --> projeccions de valors

### 1) 'category-axis'      --> 'x-axis'
### 2) 'region-color'       --> 'legend'
### 3) 'primary-values'     --> 'y-axis'


from viz_types.models.viz_types_models import get_available_visualizations as gv
from importlib import import_module

def get_feed_definitions(id: str):
    """
    Retorna la definició de la gràfica seleccionada.
    L'estructura sempre ha de ser un diccionari amb 1 clau
    'feed' on incorporarem com arrays els diferents camps.
    """

    feed_definition_module = import_module(f"feed_definitions.models.tools.{id}")
    feed_definition = feed_definition_module.definition

    return feed_definition

