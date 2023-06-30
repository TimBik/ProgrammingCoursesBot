import logging
import os


from tg_bot import config

def get_logging(file_name):
    dir_path = config.dir_path
    logger = logging.getLogger(file_name)
    if not os.path.isdir(f"{dir_path}/logs"):
        os.mkdir(f"{dir_path}/logs")
    handler = logging.FileHandler(filename=f'{dir_path}/logs/{file_name}')
    logger.addHandler(handler)
    return logger

