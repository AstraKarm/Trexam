# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 443)
        self.verticalLayout_5 = QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_seed = QLabel(Dialog)
        self.lbl_seed.setObjectName(u"lbl_seed")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        self.lbl_seed.setFont(font)

        self.verticalLayout.addWidget(self.lbl_seed)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lndt_seed = QLineEdit(Dialog)
        self.lndt_seed.setObjectName(u"lndt_seed")
        self.lndt_seed.setFont(font)

        self.horizontalLayout_2.addWidget(self.lndt_seed)

        self.pshbttn_addseed = QPushButton(Dialog)
        self.pshbttn_addseed.setObjectName(u"pshbttn_addseed")
        self.pshbttn_addseed.setMinimumSize(QSize(112, 0))
        self.pshbttn_addseed.setMaximumSize(QSize(112, 16777215))
        self.pshbttn_addseed.setFont(font)

        self.horizontalLayout_2.addWidget(self.pshbttn_addseed)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_types = QLabel(Dialog)
        self.lbl_types.setObjectName(u"lbl_types")
        self.lbl_types.setFont(font)

        self.verticalLayout_4.addWidget(self.lbl_types)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cmbbx_types = QComboBox(Dialog)
        self.cmbbx_types.setObjectName(u"cmbbx_types")
        self.cmbbx_types.setFont(font)

        self.horizontalLayout_3.addWidget(self.cmbbx_types)

        self.spnbx_types = QSpinBox(Dialog)
        self.spnbx_types.setObjectName(u"spnbx_types")
        self.spnbx_types.setMaximumSize(QSize(50, 16777215))
        self.spnbx_types.setMinimum(1)
        self.spnbx_types.setValue(1)

        self.horizontalLayout_3.addWidget(self.spnbx_types)

        self.pshbttn_addtypes = QPushButton(Dialog)
        self.pshbttn_addtypes.setObjectName(u"pshbttn_addtypes")
        self.pshbttn_addtypes.setMinimumSize(QSize(112, 0))
        self.pshbttn_addtypes.setMaximumSize(QSize(112, 16777215))
        self.pshbttn_addtypes.setFont(font)

        self.horizontalLayout_3.addWidget(self.pshbttn_addtypes)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_id = QLabel(Dialog)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_id)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lndt_id = QLineEdit(Dialog)
        self.lndt_id.setObjectName(u"lndt_id")
        self.lndt_id.setFont(font)

        self.horizontalLayout_5.addWidget(self.lndt_id)

        self.pshbttn_addid = QPushButton(Dialog)
        self.pshbttn_addid.setObjectName(u"pshbttn_addid")
        self.pshbttn_addid.setMinimumSize(QSize(112, 0))
        self.pshbttn_addid.setMaximumSize(QSize(112, 16777215))
        self.pshbttn_addid.setFont(font)

        self.horizontalLayout_5.addWidget(self.pshbttn_addid)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tablvw_questions = QTableView(Dialog)
        self.tablvw_questions.setObjectName(u"tablvw_questions")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setBold(False)
        self.tablvw_questions.setFont(font1)
        self.tablvw_questions.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablvw_questions.setDragEnabled(False)
        self.tablvw_questions.setDragDropOverwriteMode(False)
        self.tablvw_questions.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.tablvw_questions.setDefaultDropAction(Qt.DropAction.IgnoreAction)

        self.verticalLayout_2.addWidget(self.tablvw_questions)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pshbttn_clear = QPushButton(Dialog)
        self.pshbttn_clear.setObjectName(u"pshbttn_clear")
        self.pshbttn_clear.setMinimumSize(QSize(0, 0))
        self.pshbttn_clear.setMaximumSize(QSize(16777215, 16777215))
        self.pshbttn_clear.setFont(font)

        self.horizontalLayout_4.addWidget(self.pshbttn_clear)

        self.pshbttn_delete = QPushButton(Dialog)
        self.pshbttn_delete.setObjectName(u"pshbttn_delete")
        self.pshbttn_delete.setMinimumSize(QSize(0, 0))
        self.pshbttn_delete.setMaximumSize(QSize(16777215, 16777215))
        self.pshbttn_delete.setFont(font)

        self.horizontalLayout_4.addWidget(self.pshbttn_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.pshbttn_compile = QPushButton(Dialog)
        self.pshbttn_compile.setObjectName(u"pshbttn_compile")
        self.pshbttn_compile.setFont(font)

        self.verticalLayout_5.addWidget(self.pshbttn_compile)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_seed.setText(QCoreApplication.translate("Dialog", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None))
        self.lndt_seed.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u044e\u0447 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438 (\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043f\u0443\u0441\u0442\u044b\u043c \u0434\u043b\u044f \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0433\u043e)", None))
        self.pshbttn_addseed.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.lbl_types.setText(QCoreApplication.translate("Dialog", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0435(-\u044f) \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u0439 \u043b\u0438\u043d\u0438\u0438", None))
        self.pshbttn_addtypes.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.lbl_id.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0443\u0447\u043d\u0443\u044e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.lndt_id.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None))
        self.pshbttn_addid.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pshbttn_clear.setText(QCoreApplication.translate("Dialog", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pshbttn_delete.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pshbttn_compile.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

