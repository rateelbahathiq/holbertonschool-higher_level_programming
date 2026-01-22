#!/usr/bin/python3
"""
Prints all City objects from the database, ordered by city id,
displayed with their corresponding State name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_cities_by_state(username, password, database):
    """
    Connects to the database and prints all cities
    with their associated state names.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()


if __name__ == "__main__":
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
