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

        # Initialize the database connection
        self.engine = create_engine('sqlite:///rental_base.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.model = QStandardItemModel(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.load_stations()

    def load_stations(self):
        self.model.clear()

        self.model.setHorizontalHeaderLabels(["Station Name"])

        stations = self.session.query(Station).all()

        for station in stations:
            name_item = QStandardItem(station.station_name)
            self.model.appendRow([name_item])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
