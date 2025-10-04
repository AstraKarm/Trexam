from os.path import isdir, isfile
from os import getenv, makedirs
import configparser

class DataHandler():
    def __init__(self):
        self.create_folder()
        self.create_download_folder()
        self.load_config()
        self.load_script()

    def create_folder(self):
        self.path = getenv('APPDATA') + '\\Trexam'

        if not isdir(self.path):
            makedirs(self.path)

    def create_download_folder(self):
        self.downloads_path = self.path + '\\downloads'

        if not isdir(self.downloads_path):
            makedirs(self.downloads_path)

    def load_config(self):
        self.config_path = self.path + '\\config.ini'
        self.config = configparser.ConfigParser()

        if not isfile(self.config_path):
            f = open(self.config_path, 'w+')
            self.config.read(self.config_path)

            self.config.add_section('Browser')
            self.config.set('Browser', 'scale', '1.0')
            self.config.add_section('Keys')
            self.config.set('Keys', 'key_0', '1060')
            self.config.set('Keys', 'key_1', '1042')
            self.config.set('Keys', 'key_2', '16777220')
            self.config.set('Keys', 'key_3', '1050')
            self.config.write(f)
            f.close()

        f = open(self.config_path, 'r')
        self.config.read(self.config_path)
        f.close()

    def load_script(self):
        f = open('extra\\runtime\\script.js')
        self.script = f.read()
        f.close()

    def save_config(self):
        f = open(self.config_path, 'w')
        self.config.write(f)
        f.close()
