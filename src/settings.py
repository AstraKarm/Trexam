import src.extensions as ex
from src.ui_settings import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtCore import Qt
import webbrowser

class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.key_buttons = []
        self.key_buttons.append(self.ui.pshbttn_prevquestion)
        self.key_buttons.append(self.ui.pshbttn_nextquestion)
        self.key_buttons.append(self.ui.pshbttn_confirm)
        self.key_buttons.append(self.ui.pshbttn_refresh)

        self.current_key = -1

        # Настройки окна
        self.setWindowTitle('Настройки')
        self.setWindowIcon(QIcon('extra\\runtime\\icon.png'))
        self.setFixedSize(self.width(), self.height())

        # Загрузка настроек
        self.ui.spnbx_scale.setValue(float(ex.data_handler.config.get('Browser', 'scale')) * 100)

        for i in range(0, 4):
            text = Qt.Key(int(ex.data_handler.config.get('Keys', f'Key_{i}'))).name[4:]
            if text != '':
                self.key_buttons[i].setText(Qt.Key(int(ex.data_handler.config.get('Keys', f'Key_{i}'))).name[4:])
            else:
                self.key_buttons[i].setText(QKeySequence(int(ex.data_handler.config.get('Keys', f'Key_{i}'))).toString())

        # Сигналы
        self.key_buttons[0].clicked.connect(self.key_button_0)
        self.key_buttons[1].clicked.connect(self.key_button_1)
        self.key_buttons[2].clicked.connect(self.key_button_2)
        self.key_buttons[3].clicked.connect(self.key_button_3)
        self.ui.pshbttn_authorpage.clicked.connect(self.btn_author)
        self.ui.pshbttn_bank.clicked.connect(self.btn_bank_fipi)

        self.key_buttons[0].clearFocus()

        self.show()

    def key_button_0(self):
        if self.current_key == -1:
            self.current_key = 0
            self.key_buttons[0].setText('Выберите кнопку')
            self.key_buttons[0].clearFocus()

    def key_button_1(self):
        if self.current_key == -1:
            self.current_key = 1
            self.key_buttons[1].setText('Выберите кнопку')
            self.key_buttons[1].clearFocus()

    def key_button_2(self):
        if self.current_key == -1:
            self.current_key = 2
            self.key_buttons[2].setText('Выберите кнопку')
            self.key_buttons[2].clearFocus()

    def key_button_3(self):
        if self.current_key == -1:
            self.current_key = 3
            self.key_buttons[3].setText('Выберите кнопку')
            self.key_buttons[3].clearFocus()

    def btn_author(self):
        webbrowser.open('https://github.com/AstraKarm/Trexam')

    def btn_bank_fipi(self):
        webbrowser.open('https://fipi.ru/')

    def keyPressEvent(self, event):
        text = Qt.Key(event.key()).name[4:]

        if self.current_key != -1:
            if text != '':
                self.key_buttons[self.current_key].setText(text)
            else:
                self.key_buttons[self.current_key].setText(event.text().capitalize())

        ex.data_handler.config.set('Keys', f'Key_{self.current_key}', str(event.key()))
        self.current_key = -1

    def closeEvent(self, arg__1):
        ex.data_handler.config.set('Browser', 'scale', str(self.ui.spnbx_scale.value() / 100))
        ex.data_handler.save_config()
        ex.main_window.ui.wbngnvw_browser.setZoomFactor(self.ui.spnbx_scale.value() / 100)