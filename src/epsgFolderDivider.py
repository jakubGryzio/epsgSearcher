import os
import shutil
from PathCreator import PathCreator
from epsgSearcher import espgSearcher
from helpers.logger import copy_done_logger, error_logger
from helpers.config import OUTPUT_DWG_FOLDER_PATH


class EpsgFolderDivider():
    DWG_EXTENSION = '.dwg'
    OUTPUT_DWG_FOLDER = os.path.join(OUTPUT_DWG_FOLDER_PATH, 'IN--WROCLAW')
    OUTPUT_RAMKI_FOLDER = os.path.join(
        OUTPUT_DWG_FOLDER_PATH, 'IN--RAMKI--WROCLAW')

    def __init__(self, epsgSearcher: espgSearcher = None, pathCreator: PathCreator = None):
        self.epsgSearcher = epsgSearcher
        if pathCreator is None:
            self.pathCreator = epsgSearcher.pathCreator
        else:
            self.pathCreator = pathCreator
        self.error = False

    def __make_parent_directory(self, is_ramki=None):
        parent_folder_path = self.OUTPUT_DWG_FOLDER
        if is_ramki:
            parent_folder_path = self.OUTPUT_RAMKI_FOLDER
        if not os.path.exists(parent_folder_path):
            os.makedirs(parent_folder_path, mode=0o777, exist_ok=False)
        return parent_folder_path

    def __make_child_directory(self, parent_directory, name):
        child_folder_path = os.path.join(parent_directory, name)
        if not os.path.exists(child_folder_path):
            os.makedirs(child_folder_path, mode=0o777, exist_ok=False)
        return child_folder_path

    def __make_another_folder(self, parent_directory, filename_item):
        another_folder_path = parent_directory
        another_folder_idx = 2
        for elem in filename_item[another_folder_idx:-1]:
            another_folder_path = self.__make_child_directory(
                another_folder_path, elem)
        return another_folder_path

    def __copy_dwg_file(self, const, source, destination):
        _, file_extension = os.path.splitext(source)
        source = source.replace(file_extension, self.DWG_EXTENSION)
        sourcePath = const + source
        try:
            shutil.copy(sourcePath, destination)
            copy_done_logger(self.pathCreator.filename)
        except Exception as e:
            self.error = True
            error_logger(e)

    def make_epsg_folders(self, source_directory, epsg=None, is_ramki=False):
        parent_folder_path = self.__make_parent_directory(is_ramki)
        if self.epsgSearcher is not None:
            epsg = self.epsgSearcher.epsg
        epsg_folder_path = self.__make_child_directory(
            parent_folder_path, f'EPSG--{epsg}')

        filename_item = self.pathCreator.split_filename
        dwg_file_path = self.pathCreator.dwg_file_path

        set_folder_path = self.__make_child_directory(
            epsg_folder_path, self.pathCreator.set_folder_path)
        line_folder_path = self.__make_child_directory(
            set_folder_path, self.pathCreator.line_folder_path)

        valid_folder_path_length = 3

        if len(filename_item) != valid_folder_path_length:
            another_folder_path = self.__make_another_folder(
                line_folder_path, filename_item)
            self.__copy_dwg_file(
                source_directory, dwg_file_path, another_folder_path)
        else:
            self.__copy_dwg_file(
                source_directory, dwg_file_path, line_folder_path)
