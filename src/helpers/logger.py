import logging
import os
from datetime import date, datetime
from .config import LOG_FILE_PATH


def execute_logger(pathCreator, counter, length):
    log_path = os.path.join(LOG_FILE_PATH, f"infoEPSG_{date.today()}.log")
    try:
        os.remove(log_path)
    except OSError:
        pass
    log_format = '%(asctime)s | %(levelname)s | %(message)s'
    log_level = logging.INFO
    logging.basicConfig(filename=log_path, level=log_level, format=log_format)

    logging.info(f'READ DXF: {counter + 1}/{length} {pathCreator.filename}')
    print(f'{datetime.now().strftime("%H:%M:%S")} |DONE-READ_DXF| {counter + 1}/{length} {pathCreator.filename}')


def copy_done_logger(filename):
    print(f'{datetime.now().strftime("%H:%M:%S")} |DONE-COPY_DWG| {filename}')
    logging.info(f'COPY DWG: {filename}')


def error_logger(error):
    logging.error(error)


def done_logger():
    logging.info(f'-------------- Processing was done --------------')
