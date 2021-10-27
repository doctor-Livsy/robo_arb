import logging


def get_file_handler():
    file_handler = logging.FileHandler("events.log")
    file_handler.setLevel(logging.INFO)
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    return logger
