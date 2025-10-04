# Приложение
import src.extensions as ex
from src.ui_generator import Ui_Dialog

# PySide6
from PySide6.QtWidgets import QDialog
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QAbstractItemView

# Дополнительные
import random
from datetime import datetime

class Generator(QDialog):
    def __init__(self):
        super(Generator, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Настройки окна
        self.setWindowTitle('Составить свой вариант КИМ')
        self.setWindowIcon(QIcon('extra\\runtime\\icon.png'))
        self.setFixedSize(self.width(), self.height())

        # Сигналы
        self.ui.pshbttn_addseed.clicked.connect(self.addseed)
        self.ui.pshbttn_addtypes.clicked.connect(self.addtype)
        self.ui.pshbttn_addid.clicked.connect(self.addid)
        self.ui.pshbttn_clear.clicked.connect(self.clear)
        self.ui.pshbttn_delete.clicked.connect(self.delete)
        self.ui.pshbttn_compile.clicked.connect(self.compile)
        self.ui.cmbbx_types.currentIndexChanged.connect(self.typesupdated)

        # Загрузка типов
        for i in range(ex.main_window.ui.cmbbx_type.count() - 1):
            self.ui.cmbbx_types.addItem(ex.main_window.ui.cmbbx_type.itemText(i))
        
        # Модель
        self.model = QStandardItemModel()
        self.model.insertColumn(1)
        self.model.setHorizontalHeaderLabels(['Тип задания', 'Идентификатор'])
        self.ui.tablvw_questions.setModel(self.model)
        self.ui.tablvw_questions.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        #Типы
        self.typesupdated()

        self.show()

    def typesupdated(self):
        f = open(f'proj\\{ex.main_window.proj}\\{self.ui.cmbbx_types.currentText()}.txt')
        self.questions = f.read().split('\n')
        f.close()

        self.ui.spnbx_types.setMaximum(len(self.questions))

    def addseed(self):
        seed = self.ui.lndt_seed.text()

        if seed != '':
            random.seed(seed)
        else:
            random.seed(datetime.now().timestamp())

        group = ''
        for i in ex.main_window.types:
            f = open(f'proj\\{ex.main_window.proj}\\{i}.txt')
            content = f.read()
            f.close()

            if content.find('-') != -1:
                if group == '':
                    id = random.choice(content.split('\n'))
                    group = id[7 : 13]
                else:
                    id = random.choice([x for x in content.split('\n') if x.endswith(group)])
            else:
                id = random.choice(content.split('\n'))
                group = ''

            item1 = QStandardItem(i)
            item2 = QStandardItem(id)
            self.model.appendRow([item1, item2])

    def addtype(self):
        type = self.ui.cmbbx_types.currentText()

        content = self.questions

        for i in range(self.ui.spnbx_types.value()):
            question = random.choice(content)
            content.remove(question)
            self.model.appendRow([QStandardItem(type), QStandardItem(question)])

    def addid(self):
        id = self.ui.lndt_id.text()
        type = ''

        if id == '':
            return

        for i in ex.main_window.types:
            f = open(f'proj\\{ex.main_window.proj}\\{i}.txt')
            content = f.read().split('\n')
            f.close()

            if id in content:
                type = i

        if type != '':
            item1 = QStandardItem(type)
            item2 = QStandardItem(id)
            self.model.appendRow([item1, item2])
        else:
            self.ui.lndt_id.setText('Такого задания нет!')

    def clear(self):
        self.model.clear()
        self.model.insertColumn(1)
        self.model.setHorizontalHeaderLabels(['Тип задания', 'Идентификатор'])

    def delete(self):
        selected_rows = self.ui.tablvw_questions.selectionModel().selectedRows()
        try:
            self.model.removeRows(selected_rows[0].row(), len(selected_rows))
        except:
            selected_indexes = self.ui.tablvw_questions.selectionModel().selectedIndexes()
            self.model.removeRows(selected_indexes[0].row(), len(selected_indexes))

    def compile(self):
        ex.main_window.questions = []

        for i in range(self.model.rowCount()):
            ex.main_window.questions.append(self.model.index(i, 1).data())

        ex.main_window.currentQuestion = 0
        ex.main_window.load_question()
        self.close()