from viz_types.models.viz_types_models import get_available_visualizations
from fastapi import HTTPException

def validate_viz_id(id):
    
    
    visualizations = dict(get_available_visualizations())
    
    viz_ids = [dict(x)["id"] for x in visualizations["visualizations"]]

    if id not in viz_ids:
        raise HTTPException(status_code=404,detail="Viz Id not found")
        return
    
    return id
