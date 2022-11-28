import os


class PathCreator:
    def __init__(self, dxf_directory, path, dxf_file):
        self.dxf_directory = dxf_directory
        self.path = path
        self.dxf_file = dxf_file

    @property
    def full_path(self):
        return os.path.join(self.path, self.dxf_file)

    @property
    def split_filename(self):
        filename = self.full_path.replace(
            self.dxf_directory+'\\', '')
        return filename.split('\\')

    @property
    def folderpath(self):
        no_dxf_file_path_idx = -1
        return '--'.join(self.split_filename[:no_dxf_file_path_idx])

    @property
    def filename(self):
        return '--'.join(self.split_filename)

    @property
    def dwg_file_path(self):
        return '\\' + '\\'.join(self.split_filename)

    @property
    def set_folder_path(self):
        return self.split_filename[0]

    @property
    def line_folder_path(self):
        return self.split_filename[1]

    @property
    def file_extension(self):
        _, file_extension = os.path.splitext(self.full_path)
        return file_extension

    @property
    def dwg_file(self):
        return self.dxf_file.replace(
            self.file_extension, '.dwg')
