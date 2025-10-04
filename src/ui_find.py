# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(294, 104)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_findby = QLabel(Dialog)
        self.lbl_findby.setObjectName(u"lbl_findby")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        self.lbl_findby.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_findby)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.rdbttn_num = QRadioButton(Dialog)
        self.rdbttn_num.setObjectName(u"rdbttn_num")
        self.rdbttn_num.setFont(font)

        self.horizontalLayout.addWidget(self.rdbttn_num)

        self.rdbttn_id = QRadioButton(Dialog)
        self.rdbttn_id.setObjectName(u"rdbttn_id")
        self.rdbttn_id.setFont(font)

        self.horizontalLayout.addWidget(self.rdbttn_id)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lndt_searchbar = QLineEdit(Dialog)
        self.lndt_searchbar.setObjectName(u"lndt_searchbar")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(9)
        self.lndt_searchbar.setFont(font1)
        self.lndt_searchbar.setStyleSheet(u"background-color: #FFFFFF")

        self.horizontalLayout_2.addWidget(self.lndt_searchbar)

        self.pshbttn_random = QPushButton(Dialog)
        self.pshbttn_random.setObjectName(u"pshbttn_random")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        self.pshbttn_random.setFont(font2)
        self.pshbttn_random.setStyleSheet(u"background-color: #FFFFFF")

        self.horizontalLayout_2.addWidget(self.pshbttn_random)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pshbttn_find = QPushButton(Dialog)
        self.pshbttn_find.setObjectName(u"pshbttn_find")
        self.pshbttn_find.setFont(font)
        self.pshbttn_find.setStyleSheet(u"background-color: #FFFFFF")

        self.verticalLayout.addWidget(self.pshbttn_find)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_findby.setText(QCoreApplication.translate("Dialog", u"\u0418\u0441\u043a\u0430\u0442\u044c \u043f\u043e", None))
        self.rdbttn_num.setText(QCoreApplication.translate("Dialog", u"\u043d\u043e\u043c\u0435\u0440\u0443", None))
        self.rdbttn_id.setText(QCoreApplication.translate("Dialog", u"\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u0443", None))
        self.pshbttn_random.setText("")
        self.pshbttn_find.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0439\u0442\u0438", None))
    # retranslateUi

