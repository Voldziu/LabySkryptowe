from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QSortFilterProxyModel, Qt
from gui import Ui_MainWindow
import sys
from functionalities import load_logs


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.model = QStandardItemModel(self)
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)

        self.logTableView.setModel(self.proxy_model)  # assigning model to log tableview
        self.logTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setup_connections()

    def setup_connections(self):
        self.openLogButton.clicked.connect(self.open_file)

    def open_file(self):
        path = self.logPathEdit.text()
        load_logs(path, self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
