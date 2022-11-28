from datetime import date
import pandas as pd
import os
from PathCreator import PathCreator

from epsgSearcher import espgSearcher
from helpers.config import EXCEL_LOG_FILE_PATH


class ExcelHandler():
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.__read_excel()

    def __read_excel(self):
        self.file = pd.read_excel(self.filepath)

    def search_epsg(self, pathCreator: PathCreator):
        folderpath = pathCreator.folderpath

        string_to_find = folderpath + f'--{pathCreator.dwg_file}'

        row = self.file[self.file['PLIK'].str.contains(
            string_to_find)]

        epsg = row['EPSG_SOURCE']
        return str(int(epsg.values[0])) if epsg.values else 'NOT FOUND'

    def to_excel_data_logger(self, data):
        columns = ['Filename', 'EPSG']
        excel_path = os.path.join(
            EXCEL_LOG_FILE_PATH, f'infoEPSG_{date.today()}.xlsx')

        df = pd.DataFrame(data, columns=columns)
        df.to_excel(excel_path)
