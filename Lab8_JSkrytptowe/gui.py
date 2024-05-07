# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 703)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.openLogButton = QPushButton(self.centralwidget)
        self.openLogButton.setObjectName(u"openLogButton")
        self.openLogButton.setGeometry(QRect(810, 90, 91, 31))
        self.openLogButton.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\", sans-serif;  \n"
"    font-size: 11pt;  \n"
"    font-weight: bold;  \n"
"    color: #ffffff;  \n"
"    background-color: #4a4a4a; \n"
"    border: 2px solid #6a6a6a;  \n"
"    border-radius: 8px; \n"
"    padding: 5px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a5a5a; \n"
"    border-color: #8a8a8a;  \n"
"    color: #ffffff;  \n"
"}\n"
"")
        self.logPathEdit = QLineEdit(self.centralwidget)
        self.logPathEdit.setObjectName(u"logPathEdit")
        self.logPathEdit.setGeometry(QRect(150, 90, 611, 41))
        self.fromDateEdit = QLineEdit(self.centralwidget)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setGeometry(QRect(120, 200, 113, 25))
        self.toDateEdit = QLineEdit(self.centralwidget)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setGeometry(QRect(310, 200, 113, 25))
        self.fromLabel = QLabel(self.centralwidget)
        self.fromLabel.setObjectName(u"fromLabel")
        self.fromLabel.setGeometry(QRect(60, 200, 41, 19))
        self.fromLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 12pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.toLabel = QLabel(self.centralwidget)
        self.toLabel.setObjectName(u"toLabel")
        self.toLabel.setGeometry(QRect(270, 200, 31, 19))
        self.toLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 12pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.filterButton = QPushButton(self.centralwidget)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setGeometry(QRect(500, 200, 88, 27))
        self.filterButton.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\", sans-serif;  \n"
"    font-size: 11pt;  \n"
"    font-weight: bold;  \n"
"    color: white;  \n"
"    background-color: #4a4a4a; \n"
"    border: 2px solid #6a6a6a;  \n"
"    border-radius: 8px; \n"
"    padding: 5px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a5a5a; \n"
"    border-color: #8a8a8a;  \n"
"    color: #ffffff;  \n"
"}\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(910, 620, 91, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\", sans-serif;  \n"
"    font-size: 11pt;  \n"
"    font-weight: bold;  \n"
"    color: #ffffff;  \n"
"    background-color: #4a4a4a; \n"
"    border: 2px solid #6a6a6a;  \n"
"    border-radius: 8px; \n"
"    padding: 5px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a5a5a; \n"
"    border-color: #8a8a8a;  \n"
"    color: #ffffff;  \n"
"}")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 620, 101, 31))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\", sans-serif;  \n"
"    font-size: 11pt;  \n"
"    font-weight: bold;  \n"
"    color: #ffffff;  \n"
"    background-color: #4a4a4a; \n"
"    border: 2px solid #6a6a6a;  \n"
"    border-radius: 8px; \n"
"    padding: 5px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a5a5a; \n"
"    border-color: #8a8a8a;  \n"
"    color: #ffffff;  \n"
"}")
        self.hostAddressLabel = QLabel(self.centralwidget)
        self.hostAddressLabel.setObjectName(u"hostAddressLabel")
        self.hostAddressLabel.setGeometry(QRect(720, 220, 101, 20))
        self.hostAddressLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 11pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}\n"
"")
        self.hostAddressLabel.setOpenExternalLinks(False)
        self.hostAddressEdit = QLineEdit(self.centralwidget)
        self.hostAddressEdit.setObjectName(u"hostAddressEdit")
        self.hostAddressEdit.setGeometry(QRect(840, 210, 161, 31))
        self.hostAddressEdit.setReadOnly(False)
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(720, 280, 68, 19))
        self.dateLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 11pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.dateEdit = QLineEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(840, 270, 161, 31))
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(720, 340, 68, 19))
        self.timeLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 11pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.timeEdit = QLineEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(840, 330, 161, 31))
        self.statusCodeEdit = QLineEdit(self.centralwidget)
        self.statusCodeEdit.setObjectName(u"statusCodeEdit")
        self.statusCodeEdit.setGeometry(QRect(840, 390, 161, 31))
        self.resourceEdit = QLineEdit(self.centralwidget)
        self.resourceEdit.setObjectName(u"resourceEdit")
        self.resourceEdit.setGeometry(QRect(840, 450, 161, 31))
        self.resourceLabel = QLabel(self.centralwidget)
        self.resourceLabel.setObjectName(u"resourceLabel")
        self.resourceLabel.setGeometry(QRect(720, 470, 68, 19))
        self.resourceLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 11pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.sizeEdit = QLineEdit(self.centralwidget)
        self.sizeEdit.setObjectName(u"sizeEdit")
        self.sizeEdit.setGeometry(QRect(840, 510, 161, 31))
        self.sizeLabel = QLabel(self.centralwidget)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setGeometry(QRect(720, 520, 68, 19))
        self.sizeLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 11pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.statusCodeLabel = QLabel(self.centralwidget)
        self.statusCodeLabel.setObjectName(u"statusCodeLabel")
        self.statusCodeLabel.setGeometry(QRect(720, 400, 91, 20))
        self.statusCodeLabel.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 11pt; \n"
"    color: #AD88C6;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(80, 260, 531, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 529, 319))
        self.logTableView = QTableView(self.scrollAreaWidgetContents)
        self.logTableView.setObjectName(u"logTableView")
        self.logTableView.setGeometry(QRect(10, 10, 511, 301))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 20, 191, 41))
        self.label.setStyleSheet(u"QLabel {\n"
"     font-family: \"Arial\", sans-serif; \n"
"    font-size: 20pt; \n"
"    color: white;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openLogButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.fromLabel.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.toLabel.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.hostAddressLabel.setText(QCoreApplication.translate("MainWindow", u"Host address", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.resourceLabel.setText(QCoreApplication.translate("MainWindow", u"Resource", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.statusCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Status code", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Log Explorer", None))
    # retranslateUi

