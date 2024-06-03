from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QMessageBox, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import QSortFilterProxyModel, Qt, QItemSelectionModel
import datetime
from gui import Ui_MainWindow
import sys



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Bike Rentals Analysis")
