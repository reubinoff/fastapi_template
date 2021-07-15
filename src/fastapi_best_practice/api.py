from fastapi import APIRouter
from fastapi.responses import JSONResponse

api_router = APIRouter(
    default_response_class=JSONResponse
)  # WARNING: Don't use this unless you want unauthenticated routes
authenticated_api_router = APIRouter()