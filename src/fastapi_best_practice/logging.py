import logging
import colorlog
from colorlog import ColoredFormatter

from fastapi_best_practice.config import configuration
from fastapi.logger import logger


formatter = ColoredFormatter(
	"%(log_color)s%(levelname)-8s>> %(reset)s %(blue)s%(message)s",
	datefmt=None,
	reset=True,
	log_colors={
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red,bg_white',
	},
	secondary_log_colors={},
	style='%'
)

def configure_logging(log_level=configuration.log_level):
    if log_level == "DEBUG":
        handler = colorlog.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(log_level)
        logger.handlers = []

        logger.addHandler(handler)
        
    else:
        logging.basicConfig(level=log_level)

