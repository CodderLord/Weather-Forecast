import logging
import os
from logging.handlers import RotatingFileHandler
import colorlog


def setup_logger():
    log = logging.getLogger("weather_app")
    log.setLevel(logging.DEBUG)

    # init directory for logs
    if not os.path.exists("logs"):
        os.makedirs("logs")

    file_handler = RotatingFileHandler(
        "logs/weather.log",
        maxBytes=1024 * 1024,
        backupCount=4,
        encoding="UTF-8"
    )
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))

    # Setting color for logs
    console_handler = logging.StreamHandler()
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s - %(message)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red'
        }
    )
    console_handler.setFormatter(color_formatter)

    log.addHandler(file_handler)
    log.addHandler(console_handler)
    return log


