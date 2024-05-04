import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableView, QHeaderView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QSortFilterProxyModel, Qt,QItemSelectionModel

import functionalities
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
        self.path=""

        self.logTableView.setModel(self.proxy_model)  # assigning model to log tableview
        self.logTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.logTableView.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.setup_connections()

    def setup_connections(self):
        self.openLogButton.clicked.connect(self.open_file)
        self.logTableView.clicked.connect(self.handleItemClick)
        self.pushButton_3.clicked.connect(self.getNext)
        self.pushButton_4.clicked.connect(self.getPrevious)
        self.filterButton.clicked.connect(self.filter)

    def filter(self):
        lower = self.fromDateEdit.text()
        if(lower==""):
            date_lower = datetime.datetime.min.date()
        else:

            try:
                date_lower = datetime.datetime.strptime(lower,"%d/%m/%Y").date()

            except:
                print("Wrong date encoding")
                raise TypeError("Wrong date encoding")
        upper = self.toDateEdit.text()
        if (upper == ""):
            date_upper = datetime.datetime.max.date()
        else:
            try:
                date_upper= datetime.datetime.strptime(upper,"%d/%m/%Y").date()

            except:
                print("Wrong date encoding")
                raise TypeError("Wrong date encoding")
        print(date_lower)
        print(date_upper)
        if date_lower >= date_upper:
            print("dupa")
            raise  Exception("Make dates reversed!")
        def pred(date):
            return date_lower <= date <= date_upper

        new_model = QStandardItemModel(self)
        self.model = new_model
        functionalities.load_logs(self.path,self.model,pred)
        self.proxy_model.setSourceModel(self.model)
        self.init_item()




    def handleItemClick(self,index):
        print(index)
        print(self.logTableView.model().rowCount())
        item_text = index.data(Qt.DisplayRole)
        self.analyze_item(item_text)
        self.getSelectedIndex()

    def getSelectedIndex(self):
        selection_model = self.logTableView.selectionModel()
        selected_indexes = selection_model.selectedIndexes()

        if selected_indexes:
            index = selected_indexes[0]
            print("Selected Row:", index.row(), "Column:", index.column())
        else:
            print("No item is selected.")

        return index

    def getNext(self):
        index = self.getSelectedIndex()
        selection_model = self.logTableView.selectionModel()

        if index.row()< self.logTableView.model().rowCount()-1:

            next_index = index.sibling(index.row()+1,index.column())
            selection_model.clearSelection()
            selection_model.select(next_index,QItemSelectionModel.Select)

            self.handleItemClick(next_index)
        else:
            QMessageBox.information(None, "Iteration Error", f"Don't scroll that much")
    def getPrevious(self):
        index = self.getSelectedIndex()
        selection_model = self.logTableView.selectionModel()
        if index.row() >0:
            prev_index = index.sibling(index.row() - 1, index.column())
            selection_model.clearSelection()
            selection_model.select(prev_index, QItemSelectionModel.Select)
            self.handleItemClick(prev_index)

        else:
            QMessageBox.information(None, "Iteration Error", f"Don't scroll that high")

    def init_item(self):
        first_item = self.model.index(0,0)
        selection_model = self.logTableView.selectionModel()
        selection_model.select(first_item, QItemSelectionModel.Select)
        self.handleItemClick(first_item)

    def analyze_item(self,data):
        domain, datetime, path, code, bytes = functionalities.read_one_line(data)
        date = datetime.date()
        time = datetime.time()
        self.hostAddressEdit.setText(domain)
        self.dateEdit.setText(date.strftime('%Y-%m-%d'))
        self.timeEdit.setText(time.strftime('%H:%M:%S'))
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
