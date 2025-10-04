import src.extensions as ex
from src.ui_find import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
import random
from PySide6.QtCore import QSize

class Find(QDialog):
    def __init__(self):
        super(Find, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Настройки окна
        self.setWindowTitle('Поиск')
        self.setWindowIcon(QIcon('extra\\runtime\\icon.png'))
        self.setFixedSize(self.width(), self.height())

        #Иконка
        icon = QIcon()
        icon.addFile(u"extra/icons/random.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.pshbttn_random.setIcon(icon)

        # Сигналы
        self.ui.pshbttn_find.clicked.connect(self.button_pressed)
        self.ui.rdbttn_num.clicked.connect(self.button_number_pressed)
        self.ui.rdbttn_id.clicked.connect(self.button_id_pressed)
        self.ui.pshbttn_random.clicked.connect(self.button_random_pressed)

        # Стартовые функции
        self.button_number_pressed()
        self.ui.rdbttn_num.setChecked(True)
        self.show()

    def button_pressed(self):
        found = False
        text = self.ui.lndt_searchbar.text()
        if self.by_number:
            try:
                question = int(text) -1
                if question in range(0, len(ex.main_window.questions)):
                    ex.main_window.currentQuestion = int(text) -1
                    found = True
            except:
                pass
        else:
            for i in ex.main_window.questions:
                if i == text:
                    ex.main_window.currentQuestion = ex.main_window.questions.index(i)
                    found = True
        if found:
            ex.main_window.load_question()
            self.close()
        else:
            self.ui.lndt_searchbar.setText('Ничего не найдено!')

    def button_number_pressed(self):
        self.by_number = True
        self.ui.rdbttn_id.setChecked(False)
        self.ui.lndt_searchbar.setPlaceholderText(f'Пример: число от 1 до {str(len(ex.main_window.questions))}')

    def button_id_pressed(self):
        self.by_number = False
        self.ui.rdbttn_num.setChecked(False)
        self.ui.lndt_searchbar.setPlaceholderText('Пример: AB12CD')

    def button_random_pressed(self):
        ex.main_window.currentQuestion = random.randint(0, len(ex.main_window.questions))
        ex.main_window.load_question()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == int(ex.data_handler.config.get('Keys', 'Key_2')):
            self.button_pressed()