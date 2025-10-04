# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(303, 393)
        Dialog.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.grpbx_browser = QGroupBox(Dialog)
        self.grpbx_browser.setObjectName(u"grpbx_browser")
        self.grpbx_browser.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.grpbx_browser.setFont(font)
        self.verticalLayout = QVBoxLayout(self.grpbx_browser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_scale = QLabel(self.grpbx_browser)
        self.lbl_scale.setObjectName(u"lbl_scale")
        self.lbl_scale.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_scale)

        self.spnbx_scale = QSpinBox(self.grpbx_browser)
        self.spnbx_scale.setObjectName(u"spnbx_scale")
        self.spnbx_scale.setFont(font)
        self.spnbx_scale.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.spnbx_scale.setMinimum(25)
        self.spnbx_scale.setMaximum(500)
        self.spnbx_scale.setValue(100)

        self.horizontalLayout.addWidget(self.spnbx_scale)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.grpbx_browser)

        self.grpbx_keys = QGroupBox(Dialog)
        self.grpbx_keys.setObjectName(u"grpbx_keys")
        self.grpbx_keys.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.grpbx_keys)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_prevquestion = QLabel(self.grpbx_keys)
        self.lbl_prevquestion.setObjectName(u"lbl_prevquestion")
        self.lbl_prevquestion.setFont(font)

        self.horizontalLayout_2.addWidget(self.lbl_prevquestion)

        self.pshbttn_prevquestion = QPushButton(self.grpbx_keys)
        self.pshbttn_prevquestion.setObjectName(u"pshbttn_prevquestion")
        self.pshbttn_prevquestion.setFont(font)
        self.pshbttn_prevquestion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_prevquestion.setStyleSheet(u"background-color: #FFFFFF")
        self.pshbttn_prevquestion.setCheckable(False)
        self.pshbttn_prevquestion.setChecked(False)

        self.horizontalLayout_2.addWidget(self.pshbttn_prevquestion)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_nextquestion = QLabel(self.grpbx_keys)
        self.lbl_nextquestion.setObjectName(u"lbl_nextquestion")
        self.lbl_nextquestion.setFont(font)

        self.horizontalLayout_3.addWidget(self.lbl_nextquestion)

        self.pshbttn_nextquestion = QPushButton(self.grpbx_keys)
        self.pshbttn_nextquestion.setObjectName(u"pshbttn_nextquestion")
        self.pshbttn_nextquestion.setFont(font)
        self.pshbttn_nextquestion.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_nextquestion.setStyleSheet(u"background-color: #FFFFFF")
        self.pshbttn_nextquestion.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.pshbttn_nextquestion)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_confirm = QLabel(self.grpbx_keys)
        self.lbl_confirm.setObjectName(u"lbl_confirm")
        self.lbl_confirm.setFont(font)

        self.horizontalLayout_11.addWidget(self.lbl_confirm)

        self.pshbttn_confirm = QPushButton(self.grpbx_keys)
        self.pshbttn_confirm.setObjectName(u"pshbttn_confirm")
        self.pshbttn_confirm.setFont(font)
        self.pshbttn_confirm.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_confirm.setStyleSheet(u"background-color: #FFFFFF")
        self.pshbttn_confirm.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.pshbttn_confirm)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_refresh = QLabel(self.grpbx_keys)
        self.lbl_refresh.setObjectName(u"lbl_refresh")
        self.lbl_refresh.setFont(font)

        self.horizontalLayout_13.addWidget(self.lbl_refresh)

        self.pshbttn_refresh = QPushButton(self.grpbx_keys)
        self.pshbttn_refresh.setObjectName(u"pshbttn_refresh")
        self.pshbttn_refresh.setFont(font)
        self.pshbttn_refresh.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_refresh.setStyleSheet(u"background-color: #FFFFFF")
        self.pshbttn_refresh.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.pshbttn_refresh)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)


        self.verticalLayout_3.addWidget(self.grpbx_keys)

        self.grpbox_about = QGroupBox(Dialog)
        self.grpbox_about.setObjectName(u"grpbox_about")
        self.grpbox_about.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.grpbox_about)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pshbttn_authorpage = QPushButton(self.grpbox_about)
        self.pshbttn_authorpage.setObjectName(u"pshbttn_authorpage")
        self.pshbttn_authorpage.setFont(font)
        self.pshbttn_authorpage.setStyleSheet(u"background-color: #FFFFFF")

        self.verticalLayout_2.addWidget(self.pshbttn_authorpage)

        self.pshbttn_bank = QPushButton(self.grpbox_about)
        self.pshbttn_bank.setObjectName(u"pshbttn_bank")
        self.pshbttn_bank.setFont(font)
        self.pshbttn_bank.setStyleSheet(u"background-color: #FFFFFF")

        self.verticalLayout_2.addWidget(self.pshbttn_bank)

        self.lbl_version = QLabel(self.grpbox_about)
        self.lbl_version.setObjectName(u"lbl_version")
        self.lbl_version.setFont(font)
        self.lbl_version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_version)


        self.verticalLayout_3.addWidget(self.grpbox_about)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.grpbx_browser.setTitle(QCoreApplication.translate("Dialog", u"\u0411\u0440\u0430\u0443\u0437\u0435\u0440", None))
        self.lbl_scale.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431:", None))
        self.spnbx_scale.setSuffix(QCoreApplication.translate("Dialog", u"%", None))
        self.grpbx_keys.setTitle(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u043a\u043b\u0430\u0432\u0438\u0448", None))
        self.lbl_prevquestion.setText(QCoreApplication.translate("Dialog", u"\u041a \u043f\u0440\u0435\u0434. \u0437\u0430\u0434\u0430\u043d\u0438\u044e", None))
        self.pshbttn_prevquestion.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0430\u0432\u0438\u0448\u0430", None))
        self.lbl_nextquestion.setText(QCoreApplication.translate("Dialog", u"\u041a \u0441\u043b\u0435\u0434. \u0437\u0430\u0434\u0430\u043d\u0438\u044e", None))
        self.pshbttn_nextquestion.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0430\u0432\u0438\u0448\u0430", None))
        self.lbl_confirm.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.pshbttn_confirm.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0430\u0432\u0438\u0448\u0430", None))
        self.lbl_refresh.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.pshbttn_refresh.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0430\u0432\u0438\u0448\u0430", None))
        self.grpbox_about.setTitle(QCoreApplication.translate("Dialog", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.pshbttn_authorpage.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u0439 \u043d\u0430 GitHub", None))
        self.pshbttn_bank.setText(QCoreApplication.translate("Dialog", u"\u0421\u0430\u0439\u0442 \u0424\u0418\u041f\u0418", None))
        self.lbl_version.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0441\u0438\u044f 0.2.0", None))
    # retranslateUi

