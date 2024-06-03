import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from create_database import Station, Base, Rental
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
        self.calculate_statistics(int(item_id.text()))

    def calculate_statistics(self, station_id):

        avg_start_duration = self.session.query(
            func.avg(func.julianday(Rental.end_time) - func.julianday(Rental.start_time))
        ).filter(Rental.rental_station_id == station_id).scalar()

        avg_end_duration = self.session.query(
            func.avg(func.julianday(Rental.end_time) - func.julianday(Rental.start_time))
        ).filter(Rental.return_station_id == station_id).scalar()

        unique_bikes = self.session.query(
            func.count(func.distinct(Rental.bike_number))
        ).filter(
            (Rental.rental_station_id == station_id) | (Rental.return_station_id == station_id)
        ).scalar()

        print(avg_start_duration)
        print(avg_end_duration)
        print(unique_bikes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
