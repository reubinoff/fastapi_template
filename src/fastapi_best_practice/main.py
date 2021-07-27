
from fastapi_versioning import VersionedFastAPI

from fastapi import FastAPI

from fastapi_best_practice.logging import configure_logging
from fastapi_best_practice.extentions import configure_extensions
from fastapi_best_practice.api import api_router
from fastapi_best_practice.middlewares import get_middlewares
from fastapi_best_practice.config import configuration
from fastapi_best_practice.database.core import engine
from fastapi_best_practice.database.manage import init_database
from fastapi.logger import logger


# we configure the logging level and format
configure_logging()
# we configure the extensions such as Sentry
configure_extensions()

init_database(engine=engine)
# we create the Web API framework
app = FastAPI(middleware=get_middlewares())

# we add all API routes to the Web API framework
app.include_router(api_router)

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/api/v{major}',
    description='Greet users with a nice message',
    enable_latest=True,
    middleware=get_middlewares()
)

logger.info(f"Start the application: {configuration.app_name} running on env: {configuration.env}")
logger.info(f"connect to DB: {configuration.db_name}")
