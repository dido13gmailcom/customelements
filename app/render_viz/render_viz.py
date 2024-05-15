from fastapi import APIRouter, Depends, Request,Response,BackgroundTasks
from _middleware.validate_viz_id import validate_viz_id
from render_viz.models.feed import Feed
from render_viz.validators.validate_json_feed import validate_json_feed
from traceback import print_exc

router: APIRouter = APIRouter()

@router.post("/{id}/render")
async def render_viz(req: Request, bg_task: BackgroundTasks, id:str = Depends(validate_viz_id)):

    try:
        json_feed: dict = await req.json()
        headers: dict   = req.headers
        
        validation: list = validate_json_feed(json_feed)
        
        if len(validation) > 0:
            raise Exception("\n".join(validation))
        
        #######################################
        #LA classe important
        feed:Feed = Feed(id, json_feed, headers)
        #######################################
        
    except Exception as e:
        print_exc()
        return Response(status_code=200,content="""<div style="font-weight: 400;font-size: 1.2rem;font-family:helvetica;margin:auto">Dades o opcions d'entrada amb errors</div>""")
    else:
        custom_element = feed.get_custom_element(bg_task)
        return custom_element