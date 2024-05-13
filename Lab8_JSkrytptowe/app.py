from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QMessageBox, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import QSortFilterProxyModel, Qt, QItemSelectionModel
import datetime
from gui import Ui_MainWindow
import sys
from functionalities import load_logs, pred, read_one_line
from constants import time_format, date_edit_format


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Log Explorer")
        self.setupUi(self)
        self.model = QStandardItemModel(self)
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        self.path = ""

        self.logTableView.setModel(self.proxy_model)  # assigning model to log tableview
        self.logTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.logTableView.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.setup_connections()

    def setup_connections(self):
        self.openLogButton.clicked.connect(self.open_file)
        self.logTableView.clicked.connect(self.handle_item_click)
        self.pushButton_3.clicked.connect(self.get_next)
        self.pushButton_4.clicked.connect(self.get_previous)
        self.filterButton.clicked.connect(self.filter)

    def filter(self):
        lower = self.fromDateEdit.date()
        date_lower = datetime.date(lower.year(), lower.month(), lower.day())

        upper = self.toDateEdit.date()
        date_upper = datetime.date(upper.year(), upper.month(), upper.day())

        print(date_lower)
        print(date_upper)
        if date_lower >= date_upper:
            raise Exception("Make dates reversed!")

        new_model = QStandardItemModel()
        self.model = new_model
        load_logs(self.path, self.model, pred, date_lower, date_upper)
        self.proxy_model.setSourceModel(self.model)
        self.init_item()

    def handle_item_click(self, index):
        print(index)
        print(self.logTableView.model().rowCount())
        item_text = index.data(Qt.DisplayRole)
        self.analyze_item(item_text)
        self.get_selected_index()

    def get_selected_index(self):
        selection_model = self.logTableView.selectionModel()
        selected_indexes = selection_model.selectedIndexes()

        if selected_indexes:
            index = selected_indexes[0]
            print("Selected Row:", index.row(), "Column:", index.column())
        else:
            print("No item is selected.")

        return index

    def get_next(self):
        index = self.get_selected_index()
        selection_model = self.logTableView.selectionModel()

        if index.row() < self.logTableView.model().rowCount() - 1:

            next_index = index.sibling(index.row() + 1, index.column())
            selection_model.clearSelection()
            selection_model.select(next_index, QItemSelectionModel.Select)

            self.handle_item_click(next_index)
        else:
            QMessageBox.information(None, "Iteration Error", f"Don't scroll that much")

    def get_previous(self):
        index = self.get_selected_index()
        selection_model = self.logTableView.selectionModel()
        if index.row() > 0:
            prev_index = index.sibling(index.row() - 1, index.column())
            selection_model.clearSelection()
            selection_model.select(prev_index, QItemSelectionModel.Select)
            self.handle_item_click(prev_index)

        else:
            QMessageBox.information(None, "Iteration Error", f"Don't scroll that high")

    def init_item(self):
        first_item = self.model.index(0, 0)
        selection_model = self.logTableView.selectionModel()
        selection_model.select(first_item, QItemSelectionModel.Select)
        self.handle_item_click(first_item)

    def analyze_item(self, data):
        domain, datetime, path, code, bytes = read_one_line(data)
        date = datetime.date()
        time = datetime.time()
        self.hostAddressEdit.setText(domain)
        self.dateEdit.setText(date.strftime(date_edit_format))
        self.timeEdit.setText(time.strftime(time_format))
        self.statusCodeEdit.setText(str(code))
        self.sizeEdit.setText(str(bytes))
        self.resourceEdit.setText(path)

    def open_file(self):
        self.path = self.logPathEdit.text()
        load_logs(self.path, self.model)
        self.init_item()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
