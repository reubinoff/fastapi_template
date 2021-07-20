import logging 

import sentry_sdk
from fastapi.logger import logger
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.stdlib import StdlibIntegration
from sentry_sdk.integrations.excepthook import ExcepthookIntegration

from fastapi_best_practice.config import configuration

sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
)


def configure_extensions():
    logger.debug("Configuring extensions...")
    if configuration.sentry_dsn:
        sentry_sdk.init(
            dsn=str(configuration.sentry_dsn),
            integrations=[
                AioHttpIntegration(),
                ExcepthookIntegration(),
                SqlalchemyIntegration(),
                StdlibIntegration(),
                sentry_logging,
            ],
            environment=configuration.env,
            auto_enabling_integrations=False,
        )
 
 