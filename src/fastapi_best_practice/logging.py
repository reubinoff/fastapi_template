import logging

from fastapi_best_practice.config import configuration


def configure_logging(log_level=configuration.log_level):
    if log_level == "DEBUG":
        LOGFORMAT = "%(levelname)s:%(message)s:%(pathname)s:%(funcName)s:%(lineno)d"
        logging.basicConfig(level=log_level, format=LOGFORMAT)
    else:
        logging.basicConfig(level=log_level)
