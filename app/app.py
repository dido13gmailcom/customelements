import sys
sys.dont_write_bytecode = True

from fastapi import FastAPI
import uvicorn

from router import router as enrutador
from formats.formats import router as formats_endpoint

# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# from _middleware.capture_logs import CaptureLogs

from _examples.metadata.tags_metadata import tags_metadata
from _middleware.limit_body_size import LimitUploadSize
from _middleware.check_origin import CheckOrigin

# Iniciem l'app
app: FastAPI = FastAPI(
    title="Custom Elements BO CatSalut", 
    description="Documentació tècnica de l'API pels Custom Elements del BO",
    version="1",
    openapi_tags=tags_metadata)

#app.add_middleware(TrustedHostMiddleware,allowed_hosts=["localhost"])
#app.add_middleware(CaptureLogs)
app.add_middleware(LimitUploadSize, max_upload_size = 20971520)
#app.add_middleware(CheckOrigin,white_list=["127.0.0.1"])

# Enturadors
## Mapes
app.include_router(enrutador, 
                   prefix="/maps/api/visualizations", 
                   tags=["Endpoints"])



app.include_router(formats_endpoint,
                   tags=["Endpoints"])
 
# Per desenvolupament (test)
if __name__ == "__main__":

    # Iniciem el servidor de proves
    uvicorn.run("app:app",
                host="0.0.0.0",
                port=5546, 
                workers=1, 
                reload=True) 