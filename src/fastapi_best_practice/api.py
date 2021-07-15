from fastapi import APIRouter, Depends
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi_best_practice.item.views import router as items_router
from fastapi_best_practice.auth.services import get_current_user

api_router = APIRouter(
    default_response_class=JSONResponse
)  # WARNING: Don't use this unless you want unauthenticated routes
authenticated_api_router = APIRouter()



# NOTE: All api routes should be authenticated by default
authenticated_api_router.include_router(
    items_router, prefix="/items", tags=["items"]
)




@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    return {"status": "ok"}


api_router.include_router(authenticated_api_router, dependencies=[Depends(get_current_user)])
