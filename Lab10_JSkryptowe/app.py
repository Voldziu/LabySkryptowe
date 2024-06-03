import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Station, Base
from gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.engine = create_engine('sqlite:///rental_base.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.model = QStandardItemModel(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.load_stations()
        self.setup_connections()

    def setup_connections(self):
        self.tableView.clicked.connect(self.handle_station_click)

    def load_stations(self):
        self.model.clear()

        self.model.setHorizontalHeaderLabels(['ID', 'Station Name'])

        stations = self.session.query(Station).all()

        for station in stations:
            id = QStandardItem(str(station.station_id))
            name_item = QStandardItem(station.station_name)
            self.model.appendRow([id, name_item])

    def handle_station_click(self, index):
        item = self.model.itemFromIndex(index)

        row = item.row()
        item_id = self.model.item(row, 0)
        print(f'Station clicked: {item_id.text()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
