import logging
import sys


def setup_logger():
    logger = logging.getLogger("backend_logger")
    logger.setLevel(logging.INFO)

    # Evitar logs duplicados
    if logger.handlers:
        return logger

    # Handler consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Formato
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
