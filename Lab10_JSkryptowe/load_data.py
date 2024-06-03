import sys

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Station, Base


def initialize_cache(session):
    stations = session.query(Station).all()
    return {station.station_name: station.station_id for station in stations}


def get_or_create_station(station_name, station_cache, session):
    if station_name in station_cache:
        return station_cache[station_name]

    station = session.query(Station).filter_by(station_name=station_name).first()

    if station is None:
        station = Station(station_name=station_name)
        session.add(station)
        session.commit()
        session.refresh(station)
        station_cache[station_name] = station.station_id
    else:
        station_cache[station_name] = station

    return station_cache[station_name]



def add_rental(data_path, session):
    data = pd.read_csv(data_path)
    rentals_data = []

    station_cache = initialize_cache(session)
    for _, row in data.iterrows():
        rental_station_id = get_or_create_station(row['Stacja wynajmu'], station_cache, session)
        return_station_id = get_or_create_station(row['Stacja zwrotu'], station_cache, session)
        rentals_data.append({
            'rental_id': row['UID wynajmu'],
            'bike_number': row['Numer roweru'],
            'start_time': row['Data wynajmu'],
            'end_time': row['Data zwrotu'],
            'rental_station_id': rental_station_id,
            'return_station_id': return_station_id
        })
    return pd.DataFrame(rentals_data)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Incorrect amount of arguments, try again')

    else:
        engine = create_engine(f'sqlite:///{sys.argv[2]}.db')
        Session = sessionmaker(bind=engine)
        db_session = Session()
        Base.metadata.create_all(engine)

        rentals = add_rental(sys.argv[1], db_session)
        rentals.to_sql('rentals', con=engine, if_exists='append', index=False)





