import logging
import logging.config
import yaml
import os


from fastapi_best_practice.config import configuration
from fastapi.logger import logger


def configure_logging(log_level=configuration.log_level) -> None:
	log_config = f"{os.path.dirname(os.path.realpath(__file__))}/logging.yml"
	with open(log_config, 'r') as stream:
		config = yaml.load(stream, Loader=yaml.FullLoader)
		config["root"]["level"] = log_level
		logging.config.dictConfig(config)
    


