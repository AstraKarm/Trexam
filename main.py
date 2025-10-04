import src.extensions as ex
from PySide6.QtWidgets import QApplication
import sys
from src.mainwindow import MainWindow
from src.download_handler import DownloadHandler
from src.data_handler import DataHandler

def main():
    ex.app = QApplication(sys.argv)
    ex.data_handler = DataHandler()
    ex.download_handler = DownloadHandler()
    ex.main_window = MainWindow()
    
    sys.exit(ex.app.exec())

if __name__ == '__main__':
    main()