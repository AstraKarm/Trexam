import src.extensions as ex
from PySide6.QtWebEngineCore import QWebEngineDownloadRequest
from PySide6.QtCore import QFileInfo
from os.path import isfile
from os import startfile

class DownloadHandler():
    def __init__(self):
        pass

    def download_requested(self, download_request: QWebEngineDownloadRequest):
        self.download_request = download_request

        # Создание имени файла
        self.filename = self.download_request.downloadFileName()
        self.filename = ex.data_handler.downloads_path + '\\' + self.filename.replace(self.filename[0 : self.filename.find('.')], ex.main_window.questions[ex.main_window.currentQuestion])

        # Если скачан, то открыть
        if isfile(self.filename):
            startfile(self.filename)
            self.download_request.cancel()
            return

        # Подготовка панели загрузки
        ex.main_window.ui.prgrssbr_download.setValue(0)
        ex.main_window.ui.prgrssbr_download.setMaximum(self.download_request.totalBytes())
        ex.main_window.ui.wdgt_download.show()
        ex.main_window.ui.lbl_message.setText(f'Загрузка файла задания {ex.main_window.questions[ex.main_window.currentQuestion]}...')

        # Последнее
        self.download_request.setDownloadDirectory(QFileInfo(ex.data_handler.downloads_path + '\\').path())
        self.download_request.setDownloadFileName(QFileInfo(self.filename).fileName())
        self.download_request.accept()
        self.download_request.receivedBytesChanged.connect(self.received_bytes_changed)
        self.download_request.isFinishedChanged.connect(self.download_finished)

    def download_pause(self):
        if not self.download_request.isPaused():
            self.download_request.pause()
        else:
            self.download_request.resume()

    def download_cancel(self):
        self.download_request.cancel()

    def received_bytes_changed(self):
        ex.main_window.ui.prgrssbr_download.setValue(self.download_request.receivedBytes())

    def download_finished(self):
        ex.main_window.ui.wdgt_download.hide()

        if isfile(self.filename):
            startfile(self.filename)

        del self.filename
        del self.download_request