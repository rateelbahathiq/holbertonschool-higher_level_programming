#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects
from the database hbtn_0e_101_usa using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State


def list_states_and_cities(username, password, database):
    """
    Connects to the database and prints all states with their cities
    using one single query.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .options(joinedload(State.cities))
        .order_by(State.id)
        .all()
    )

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    list_states_and_cities(sys.argv[1], sys.argv[2], sys.argv[3])
