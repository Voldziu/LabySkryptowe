import sys
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Station(Base):
    __tablename__ = 'stations'
    station_id = Column(Integer, primary_key=True)
    station_name = Column(String, nullable=False)


class Rental(Base):
    __tablename__ = 'rentals'
    rental_id = Column(Integer, primary_key=True)
    bike_number = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    rental_station_id = Column(Integer, ForeignKey('stations.station_id'), nullable=False)
    return_station_id = Column(Integer, ForeignKey('stations.station_id'), nullable=False)

    rental_station = relationship('Station', foreign_keys=[rental_station_id], backref='rentals_start')
    return_station = relationship('Station', foreign_keys=[return_station_id], backref='rentals_end')


def create_db(db_name):
    engine = create_engine(f'sqlite:///{db_name}.db')
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Incorrect amount of args, run the script again passing path and database name")
    else:
        create_db(sys.argv[1])
