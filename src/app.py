import os
from ExcelHandler import ExcelHandler
from PathCreator import PathCreator
from dwgFileToFolderDivider import DwgFileToFolderDivider
from epsgFolderDivider import EpsgFolderDivider
from epsgSearcher import espgSearcher
from helpers.config import EXCLUDED_DXF_FILE, EXCEL_CONFIG_FILE_PATH
from helpers.logger import execute_logger, error_logger, done_logger
from helpers.texts import epsg_error


class App():
    FILE_EXTENSION = 'DXF'

    def __init__(self, dxf_directory, dwg_directory, excelHandler):
        self.dxf_directory = dxf_directory
        self.dwg_directory = dwg_directory
        self.excelHandler = excelHandler
        self.error = False
        self.searchedFiles = self.__get_searchedFiles()
        self.log()

    def __is_valid_file(self, file):
        return (self.FILE_EXTENSION in file or self.FILE_EXTENSION.lower() in file) and file not in EXCLUDED_DXF_FILE

    def __create_epsgSearcher(self, pathCreator: PathCreator, counter, length):
        epsg_searcher = espgSearcher(pathCreator)
        execute_logger(pathCreator, counter, length)
        return epsg_searcher

    def __get_searchedFiles(self):
        epsg_Searcher_objects = []
        for currentpath, _, files in os.walk(self.dxf_directory):
            valid_files = [
                file for file in files if self.__is_valid_file(file)]
            if valid_files:
                for counter, file in enumerate(valid_files):
                    pathCreator = PathCreator(
                        self.dxf_directory, currentpath, file)
                    epsg_Searcher_object = self.__create_epsgSearcher(
                        pathCreator, counter, len(valid_files))
                    epsg_Searcher_objects.append(epsg_Searcher_object)

        return epsg_Searcher_objects

    def __check_epsg_and_make_folders(self, epsgSearcher: espgSearcher):
        divider = EpsgFolderDivider(epsgSearcher, pathCreator=None)

        epsg = epsgSearcher.check_valid_EPSG()
        if epsg == epsg_error:
            self.__change_invalid_epsg(epsgSearcher)

        divider.make_epsg_folders(self.dwg_directory)
        self.error = divider.error

        data = [epsgSearcher.pathCreator.filename, epsgSearcher.epsg]
        return data

    def __change_invalid_epsg(self, epsgSearcher: espgSearcher):
        epsgSearcher.epsg = self.excelHandler.search_epsg(
            epsgSearcher.pathCreator)

    def __compute_data(self):
        return [self.__check_epsg_and_make_folders(epsgSearcher)
                for epsgSearcher in self.searchedFiles]

    def log(self):
        if not self.searchedFiles:
            self.error = True
            error_logger("NO FILES - Something goes wrong! Check path!")
            return None
        try:
            data = self.__compute_data()
            self.excelHandler.to_excel_data_logger(data)
        except Exception as e:
            self.error = True
            error_logger(e)


if __name__ == "__main__":
    dxf_directory = input("Podaj ścieżke do katologu DXF: ")
    dwg_directory = input("Podaj ścieżke do katologu źródłowego DWG: ")
    choice = input("""-----------------------------------------
            Jeśli chcesz podzielić pliki DXF wpisz: 1
            Jeśli chcesz podzielić pliki DWG wpisz: 2
            Jeśli chcesz podzielić RAMKI wpisz: 3
    """)
    excelHandler = ExcelHandler(EXCEL_CONFIG_FILE_PATH)
    if choice == '1':
        app = App(dxf_directory, dwg_directory, excelHandler)
        if app.error:
            error_logger('Processing was done with error')
        done_logger()
        input(
            f"|DONE| Processing was done {'with error' if app.error else ''}")
    elif choice == '2':
        DwgFileToFolderDivider(dwg_directory, excelHandler).get_searchedFiles()
        input(f"|DONE| Processing was done")
    else:
        ramki_directory = input("Podaj ścieżke do katologu RAMKI: ")
        DwgFileToFolderDivider(
            ramki_directory, excelHandler).get_searchedFiles(is_ramki=True)
        input(f"|DONE| Processing was done")
