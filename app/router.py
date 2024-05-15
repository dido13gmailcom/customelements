from fastapi import APIRouter

## Galeria Custom Elements
from viz_types.viz_types import router as viz_types_router
from viz_types.viz_icons.viz_icons import router as viz_icons_router

## Opcions panel Assign data
from feed_definitions.feed_definitions import router as feed_definitions_router

## Opcions Format Chart
from render_settings.render_settings import router as render_settings_router

## Renderitzat
from render_viz.render_viz import router as render_viz_router


router: APIRouter = APIRouter()

router.include_router(viz_types_router)
router.include_router(viz_icons_router)
router.include_router(feed_definitions_router)
router.include_router(render_settings_router)
router.include_router(render_viz_router)