import os
from ExcelHandler import ExcelHandler

from PathCreator import PathCreator
from epsgFolderDivider import EpsgFolderDivider
from helpers.config import EXCLUDED_DWG_FILE


class DwgFileToFolderDivider:
    FILE_EXTENSION = 'dwg'

    def __init__(self, dwg_directory, excelHandler):
        self.dwg_directory = dwg_directory
        self.excelHandler = excelHandler

    def __is_valid_file(self, file):
        return (self.FILE_EXTENSION in file or self.FILE_EXTENSION.upper() in file) and file not in EXCLUDED_DWG_FILE

    def __divide_file(self, pathCreator: PathCreator, is_ramki):
        epsg = self.excelHandler.search_epsg(pathCreator)
        divider = EpsgFolderDivider(
            epsgSearcher=None, pathCreator=pathCreator)
        if epsg != 'NOT FOUND':
            divider.make_epsg_folders(
                self.dwg_directory, epsg=epsg, is_ramki=is_ramki)

    def get_searchedFiles(self, is_ramki=False):
        for currentpath, _, files in os.walk(self.dwg_directory):
            valid_files = [
                file for file in files if self.__is_valid_file(file)]
            if valid_files:
                for _, file in enumerate(valid_files):
                    pathCreator = PathCreator(
                        self.dwg_directory, currentpath, file)
                    self.__divide_file(pathCreator, is_ramki)
