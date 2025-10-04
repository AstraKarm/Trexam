# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 522)
        MainWindow.setStyleSheet(u"background-color: #E2E6E7")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.wdgt_topbar = QWidget(self.centralwidget)
        self.wdgt_topbar.setObjectName(u"wdgt_topbar")
        self.wdgt_topbar.setMaximumSize(QSize(16777215, 55))
        self.wdgt_topbar.setStyleSheet(u"background-color: #004147")
        self.verticalLayout_3 = QVBoxLayout(self.wdgt_topbar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_logo = QLabel(self.wdgt_topbar)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMaximumSize(QSize(130, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(28)
        font.setBold(True)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setStyleSheet(u"color: #FFFFFF")
        self.lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_logo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_proj = QLabel(self.wdgt_topbar)
        self.lbl_proj.setObjectName(u"lbl_proj")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_proj.setFont(font1)
        self.lbl_proj.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout.addWidget(self.lbl_proj)

        self.cmbbx_proj = QComboBox(self.wdgt_topbar)
        self.cmbbx_proj.setObjectName(u"cmbbx_proj")
        self.cmbbx_proj.setMinimumSize(QSize(0, 0))
        self.cmbbx_proj.setFont(font1)
        self.cmbbx_proj.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.cmbbx_proj.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout.addWidget(self.cmbbx_proj)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_type = QLabel(self.wdgt_topbar)
        self.lbl_type.setObjectName(u"lbl_type")
        self.lbl_type.setFont(font1)
        self.lbl_type.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_2.addWidget(self.lbl_type)

        self.cmbbx_type = QComboBox(self.wdgt_topbar)
        self.cmbbx_type.setObjectName(u"cmbbx_type")
        self.cmbbx_type.setFont(font1)
        self.cmbbx_type.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.cmbbx_type.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_2.addWidget(self.cmbbx_type)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.wdgt_topbar)

        self.vbxlt_browser = QVBoxLayout()
        self.vbxlt_browser.setSpacing(0)
        self.vbxlt_browser.setObjectName(u"vbxlt_browser")
        self.wdgt_navbar = QWidget(self.centralwidget)
        self.wdgt_navbar.setObjectName(u"wdgt_navbar")
        self.wdgt_navbar.setMaximumSize(QSize(16777215, 40))
        self.wdgt_navbar.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.wdgt_navbar.setStyleSheet(u"background-color: #FFFFFF")
        self.horizontalLayout_2 = QHBoxLayout(self.wdgt_navbar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pshbttn_back = QPushButton(self.wdgt_navbar)
        self.pshbttn_back.setObjectName(u"pshbttn_back")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        self.pshbttn_back.setFont(font2)
        self.pshbttn_back.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_2.addWidget(self.pshbttn_back)

        self.pshbttn_forward = QPushButton(self.wdgt_navbar)
        self.pshbttn_forward.setObjectName(u"pshbttn_forward")
        self.pshbttn_forward.setFont(font2)
        self.pshbttn_forward.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_2.addWidget(self.pshbttn_forward)

        self.pshbttn_refresh = QPushButton(self.wdgt_navbar)
        self.pshbttn_refresh.setObjectName(u"pshbttn_refresh")
        self.pshbttn_refresh.setFont(font2)
        self.pshbttn_refresh.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_refresh.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pshbttn_refresh)

        self.lbl_currentquestion = QLabel(self.wdgt_navbar)
        self.lbl_currentquestion.setObjectName(u"lbl_currentquestion")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.lbl_currentquestion.setFont(font3)

        self.horizontalLayout_2.addWidget(self.lbl_currentquestion)

        self.horizontalSpacer = QSpacerItem(310, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pshbttn_settings = QPushButton(self.wdgt_navbar)
        self.pshbttn_settings.setObjectName(u"pshbttn_settings")
        self.pshbttn_settings.setFont(font2)
        self.pshbttn_settings.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_settings.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pshbttn_settings)

        self.pshbttn_find = QPushButton(self.wdgt_navbar)
        self.pshbttn_find.setObjectName(u"pshbttn_find")
        self.pshbttn_find.setFont(font2)
        self.pshbttn_find.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_find.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pshbttn_find)

        self.pshbttn_downloads = QPushButton(self.wdgt_navbar)
        self.pshbttn_downloads.setObjectName(u"pshbttn_downloads")
        self.pshbttn_downloads.setFont(font2)
        self.pshbttn_downloads.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pshbttn_downloads.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pshbttn_downloads)


        self.vbxlt_browser.addWidget(self.wdgt_navbar)

        self.wbngnvw_browser = QWebEngineView(self.centralwidget)
        self.wbngnvw_browser.setObjectName(u"wbngnvw_browser")
        self.wbngnvw_browser.setMinimumSize(QSize(0, 341))
        self.wbngnvw_browser.setUrl(QUrl(u"about:blank"))

        self.vbxlt_browser.addWidget(self.wbngnvw_browser)

        self.wdgt_loading = QWidget(self.centralwidget)
        self.wdgt_loading.setObjectName(u"wdgt_loading")
        self.wdgt_loading.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.wdgt_loading)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_loading = QLabel(self.wdgt_loading)
        self.lbl_loading.setObjectName(u"lbl_loading")
        self.lbl_loading.setFont(font1)
        self.lbl_loading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_loading)


        self.vbxlt_browser.addWidget(self.wdgt_loading)

        self.wdgt_download = QWidget(self.centralwidget)
        self.wdgt_download.setObjectName(u"wdgt_download")
        self.wdgt_download.setMaximumSize(QSize(16777215, 30))
        self.wdgt_download.setStyleSheet(u"background-color: #FFFFFF")
        self.horizontalLayout_3 = QHBoxLayout(self.wdgt_download)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lbl_message = QLabel(self.wdgt_download)
        self.lbl_message.setObjectName(u"lbl_message")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.lbl_message.setFont(font4)

        self.horizontalLayout_3.addWidget(self.lbl_message)

        self.pshbttn_pause = QPushButton(self.wdgt_download)
        self.pshbttn_pause.setObjectName(u"pshbttn_pause")
        self.pshbttn_pause.setFont(font2)
        self.pshbttn_pause.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_3.addWidget(self.pshbttn_pause)

        self.pshbttn_stop = QPushButton(self.wdgt_download)
        self.pshbttn_stop.setObjectName(u"pshbttn_stop")
        self.pshbttn_stop.setFont(font2)
        self.pshbttn_stop.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_3.addWidget(self.pshbttn_stop)

        self.prgrssbr_download = QProgressBar(self.wdgt_download)
        self.prgrssbr_download.setObjectName(u"prgrssbr_download")
        self.prgrssbr_download.setMaximumSize(QSize(16777215, 15))
        self.prgrssbr_download.setValue(0)
        self.prgrssbr_download.setTextVisible(False)

        self.horizontalLayout_3.addWidget(self.prgrssbr_download)


        self.vbxlt_browser.addWidget(self.wdgt_download)


        self.verticalLayout_5.addLayout(self.vbxlt_browser)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"Trexam", None))
        self.lbl_proj.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442:", None))
        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u043d\u0438\u0439:", None))
        self.pshbttn_back.setText("")
        self.pshbttn_forward.setText("")
        self.pshbttn_refresh.setText("")
        self.lbl_currentquestion.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.pshbttn_settings.setText("")
        self.pshbttn_find.setText("")
        self.pshbttn_downloads.setText("")
        self.lbl_loading.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.lbl_message.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.pshbttn_pause.setText("")
        self.pshbttn_stop.setText("")
        self.prgrssbr_download.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

