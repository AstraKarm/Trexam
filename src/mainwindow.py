# Приложение
import src.extensions as ex
from src.ui_mainwindow import Ui_MainWindow
from src.find import Find
from src.settings import Settings
from src.generator import Generator

# PySide6
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QIcon

# Дополнительные
import glob
from os.path import basename
from os import startfile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Настройки окна
        self.setWindowTitle('Trexam')
        self.setWindowIcon(QIcon('extra\\runtime\\icon.png'))

        self.set_icons()
        self.connect_signals()
        self.load_proj()
        self.ui.wdgt_download.hide()

        self.show()

    # Функции
    def set_icons(self):
        icon = QIcon()
        icon.addFile(u"extra/icons/arrow_back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_back.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/arrow_forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_forward.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/refresh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_refresh.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_settings.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/find.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_find.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/downloads.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_downloads.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/play_pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_pause.setIcon(icon)

        icon = QIcon()
        icon.addFile(u"extra/icons/cancel.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_stop.setIcon(icon)

    def connect_signals(self):
        #Списки
        self.ui.cmbbx_proj.currentIndexChanged.connect(self.proj_changed)
        self.ui.cmbbx_type.currentIndexChanged.connect(self.type_changed)

        #Кнопки
        self.ui.pshbttn_back.clicked.connect(self.back)
        self.ui.pshbttn_forward.clicked.connect(self.forward)
        self.ui.pshbttn_downloads.clicked.connect(self.downloads)
        self.ui.pshbttn_refresh.clicked.connect(self.load_question)
        self.ui.pshbttn_stop.clicked.connect(ex.download_handler.download_cancel)
        self.ui.pshbttn_pause.clicked.connect(ex.download_handler.download_pause)
        self.ui.pshbttn_find.clicked.connect(self.find)
        self.ui.pshbttn_settings.clicked.connect(self.settings)

        #Браузер
        self.ui.wbngnvw_browser.loadFinished.connect(self.load_finished)

        #Загрузки
        self.ui.wbngnvw_browser.page().profile().downloadRequested.connect(ex.download_handler.download_requested)

    def load_proj(self):
        for i in glob.glob('proj\\*'):
            j = basename(i)
            if j.find('.txt') == -1:
                self.ui.cmbbx_proj.addItem(j)

        self.proj_changed()

    def proj_changed(self):
        f = open('extra\\runtime\\link_template.txt')
        self.link_template = f.read()
        f.close()

        self.proj = self.ui.cmbbx_proj.currentText()

        if self.proj.find('ОГЭ') != -1:
            self.link_template = self.link_template.replace('exam', 'oge')
        elif self.proj.find('ЕГЭ') != -1:
            self.link_template = self.link_template.replace('exam', 'ege')

        self.ui.cmbbx_type.clear()

        self.types = []
        for i in glob.glob(f'proj\\{self.proj}\\*.txt'):
            i = basename(i).replace('.txt', '')
            if i != 'proj':
                self.types.append(float(i))
        self.types.sort()

        for i in self.types:
            j = str(i).replace('.0', '')
            self.ui.cmbbx_type.addItem(j)
            self.types[self.types.index(i)] = j

        self.ui.cmbbx_type.addItem('Составить свой вариант КИМ')
        self.type_changed()

    def type_changed(self):
        self.type = self.ui.cmbbx_type.currentText()
        self.questions = []

        if self.type == '':
            return

        #Если не рандом
        if self.type != 'Составить свой вариант КИМ':
            f = open(f'proj\\{self.proj}\\{self.type}.txt')
            self.questions = f.read().split('\n')
            f.close()
            self.currentQuestion = 0
            self.load_question()
        else:
            ex.generator = Generator()

    def load_question(self):
        #Показать загрузку
        self.ui.wdgt_loading.show()
        self.ui.wbngnvw_browser.hide()

        #Отмена загрузки, если она есть
        try:
            ex.download_handler.download_cancel()
        except AttributeError:
            pass

        #Айдишник
        f = open(f'proj\\{self.proj}\\proj.txt')
        proj_id = f.read()
        f.close()

        #Создание ссылки
        link = self.link_template
        link = link.replace('&proj=', f'&proj={proj_id}')
        link = link.replace('&qid=', f'&qid={self.questions[self.currentQuestion][0 : 6]}')

        #Изменение текста
        text = 'Задание %w из %n'
        text = text.replace('%w', str(self.currentQuestion + 1)).replace('%n', str(len(self.questions)))
        self.ui.lbl_currentquestion.setText(text)

        #Переход по ссылке
        self.ui.wbngnvw_browser.load(QUrl(link))

    def load_finished(self):
        #Javascript
        self.ui.wbngnvw_browser.page().runJavaScript(ex.data_handler.script)

        self.ui.wbngnvw_browser.setZoomFactor(float(ex.data_handler.config.get('Browser', 'scale')))

        #Убрать загрузку
        self.ui.wdgt_loading.hide()
        self.ui.wbngnvw_browser.show()

    # Кнопки   
    def back(self):
        if self.currentQuestion > 0:
            self.currentQuestion -= 1
            self.load_question()

    def forward(self):
        if self.currentQuestion < len(self.questions) - 1:
            self.currentQuestion += 1
            self.load_question()

    def downloads(self):
        startfile(ex.data_handler.downloads_path)

    def find(self):
        ex.find_window = Find()

    def settings(self):
        ex.settings = Settings()

    # Комбинации клавиш
    def keyPressEvent(self, event):
        if event.key() == int(ex.data_handler.config.get('Keys', 'Key_0')):
            self.back()
        elif event.key() == int(ex.data_handler.config.get('Keys', 'Key_1')):
            self.forward()
        elif event.key() == int(ex.data_handler.config.get('Keys', 'Key_2')):
            self.ui.browser.page().runJavaScript('document.getElementsByClassName("answer-button")[0].click()')
        elif event.key() == int(ex.data_handler.config.get('Keys', 'Key_3')):
            self.load_question()