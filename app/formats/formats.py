from fastapi import APIRouter


router: APIRouter = APIRouter()

@router.get("/{domain}/api/formats")
def formats():
    return {
        "formats":[
            "text/html",
            "image/png"
        ]
    }
