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
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1057, 714)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.openLogButton = QPushButton(self.centralwidget)
        self.openLogButton.setObjectName(u"openLogButton")
        self.openLogButton.setGeometry(QRect(810, 50, 88, 27))
        self.logPathEdit = QLineEdit(self.centralwidget)
        self.logPathEdit.setObjectName(u"logPathEdit")
        self.logPathEdit.setGeometry(QRect(170, 40, 611, 41))
        self.fromDateEdit = QLineEdit(self.centralwidget)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setGeometry(QRect(110, 170, 113, 25))
        self.toDateEdit = QLineEdit(self.centralwidget)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setGeometry(QRect(310, 170, 113, 25))
        self.fromLabel = QLabel(self.centralwidget)
        self.fromLabel.setObjectName(u"fromLabel")
        self.fromLabel.setGeometry(QRect(60, 170, 41, 19))
        self.toLabel = QLabel(self.centralwidget)
        self.toLabel.setObjectName(u"toLabel")
        self.toLabel.setGeometry(QRect(270, 170, 31, 19))
        self.filterButton = QPushButton(self.centralwidget)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setGeometry(QRect(500, 170, 88, 27))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(910, 620, 91, 31))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 620, 91, 31))
        self.hostAddressLabel = QLabel(self.centralwidget)
        self.hostAddressLabel.setObjectName(u"hostAddressLabel")
        self.hostAddressLabel.setGeometry(QRect(720, 220, 101, 20))
        self.hostAddressEdit = QLineEdit(self.centralwidget)
        self.hostAddressEdit.setObjectName(u"hostAddressEdit")
        self.hostAddressEdit.setGeometry(QRect(830, 210, 131, 31))
        self.hostAddressEdit.setReadOnly(False)
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(720, 280, 68, 19))
        self.dateEdit = QLineEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(830, 270, 131, 31))
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(720, 340, 68, 19))
        self.timeEdit = QLineEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(830, 340, 131, 31))
        self.statusCodeEdit = QLineEdit(self.centralwidget)
        self.statusCodeEdit.setObjectName(u"statusCodeEdit")
        self.statusCodeEdit.setGeometry(QRect(830, 410, 141, 31))
        self.resourceEdit = QLineEdit(self.centralwidget)
        self.resourceEdit.setObjectName(u"resourceEdit")
        self.resourceEdit.setGeometry(QRect(830, 470, 141, 31))
        self.resourceLabel = QLabel(self.centralwidget)
        self.resourceLabel.setObjectName(u"resourceLabel")
        self.resourceLabel.setGeometry(QRect(730, 470, 68, 19))
        self.sizeEdit = QLineEdit(self.centralwidget)
        self.sizeEdit.setObjectName(u"sizeEdit")
        self.sizeEdit.setGeometry(QRect(830, 530, 141, 31))
        self.sizeLabel = QLabel(self.centralwidget)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setGeometry(QRect(730, 540, 68, 19))
        self.statusCodeLabel = QLabel(self.centralwidget)
        self.statusCodeLabel.setObjectName(u"statusCodeLabel")
        self.statusCodeLabel.setGeometry(QRect(720, 410, 91, 20))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1057, 33))
        MainWindow.setMenuBar(self.menubar)
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
    # retranslateUi

