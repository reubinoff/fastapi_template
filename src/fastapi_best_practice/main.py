import time
import logging
from os import path

from sentry_asgi import SentryMiddleware

from fastapi import FastAPI, Request, Response

from fastapi_best_practice.database.core import engine, sessionmaker
from fastapi_best_practice.logging import configure_logging
from fastapi_best_practice.extentions import configure_extensions
from fastapi_best_practice.api import api_router

from starlette.routing import compile_path
from starlette.middleware.base import BaseHTTPMiddleware

log = logging.getLogger(__name__)

# we configure the logging level and format
configure_logging()

# we configure the extensions such as Sentry
configure_extensions()

# we create the Web API framework
api = FastAPI(docs_url="/moshe")


def get_path_params_from_request(request: Request) -> str:
    path_params = {}
    for r in api_router.routes:
        path_regex, path_format, param_converters = compile_path(r.path)
        # remove the /api/v1 for matching
        path = f"/{request['path'].strip('/api/v1')}"
        match = path_regex.match(path)
        if match:
            path_params = match.groupdict()
    return path_params

@api.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal Server Error", status_code=500)
    try:
        path_params = get_path_params_from_request(request)

        # if this call is environment specific set the correct search path
        environment_slug = path_params.get("environment")
        if environment_slug:
            # add correct schema mapping depending on the request
            schema_engine = engine.execution_options(
                schema_translate_map={
                    None: f"environment_{environment_slug}",
                }
            )
        else:
            # add correct schema mapping depending on the request
            # can we set some default here?
            schema_engine = engine.execution_options(
                schema_translate_map={
                    None: "environment_default",
                }
            )
        session = sessionmaker(bind=schema_engine)

        if not session:
            return response

        request.state.db = session()
        request.state.environment = environment_slug
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@api.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = "max-age=31536000 ; includeSubDomains"
    return response


# we add a middleware class for logging exceptions to Sentry
api.add_middleware(SentryMiddleware)

# we add all API routes to the Web API framework
api.include_router(api_router, prefix="/api")
