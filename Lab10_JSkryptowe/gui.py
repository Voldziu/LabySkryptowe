# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QScrollArea, QSizePolicy, QStatusBar,
    QTableView, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 595)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 100, 411, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 409, 309))
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 0, 391, 301))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 60, 221, 61))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"color: #AD88C6;\n"
"font-weight: bold;  \n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 180, 231, 21))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"color: #AD88C6;\n"
"font-weight: bold;  \n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 450, 171, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"color: #AD88C6;\n"
"  font-weight: bold;  \n"
"}")
        self.startAvgTime = QTextEdit(self.centralwidget)
        self.startAvgTime.setObjectName(u"startAvgTime")
        self.startAvgTime.setGeometry(QRect(480, 110, 151, 51))
        self.startAvgTime.setReadOnly(True)
        self.finishAvgTime = QTextEdit(self.centralwidget)
        self.finishAvgTime.setObjectName(u"finishAvgTime")
        self.finishAvgTime.setGeometry(QRect(480, 210, 151, 51))
        self.finishAvgTime.setReadOnly(True)
        self.uniqueBikesAmount = QTextEdit(self.centralwidget)
        self.uniqueBikesAmount.setObjectName(u"uniqueBikesAmount")
        self.uniqueBikesAmount.setGeometry(QRect(480, 480, 61, 41))
        self.uniqueBikesAmount.setReadOnly(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 280, 111, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"color: #AD88C6;\n"
"  font-weight: bold;  \n"
"}")
        self.stationName = QTextEdit(self.centralwidget)
        self.stationName.setObjectName(u"stationName")
        self.stationName.setGeometry(QRect(480, 310, 151, 51))
        self.stationName.setReadOnly(True)
        self.amountBetween04 = QTextEdit(self.centralwidget)
        self.amountBetween04.setObjectName(u"amountBetween04")
        self.amountBetween04.setGeometry(QRect(480, 400, 61, 41))
        self.amountBetween04.setReadOnly(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 370, 251, 16))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel{\n"
"color: #AD88C6;\n"
"  font-weight: bold;  \n"
"}")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 0, 311, 51))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-size: 20pt; \n"
"    color: white;  \n"
"    font-weight: bold;  \n"
"    text-align: center; \n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 728, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Average time - start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Average time - finish", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Unique bikes parked", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Station Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Rented between 0 - 4 am", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wroclaw City Bike Stats", None))
    # retranslateUi

