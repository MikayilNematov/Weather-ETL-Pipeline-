import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """
    Skapar och returnerar en logger för hela projektet.
    Loggar både till fil (med rotation) och till terminal.

    Returns:
        logging.Logger: Logger-objektet för applikationen.
    """
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("weather_logger")
    logger.setLevel(logging.DEBUG)  #Här ger den dig din högsta detaljnivå

    if not logger.handlers:
        file_handler = RotatingFileHandler(
            "logs/app.log", maxBytes=5*1024*1024, backupCount=3, encoding="utf-8"
        )
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter("%(levelname)s - %(message)s")
        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)

    return logger
