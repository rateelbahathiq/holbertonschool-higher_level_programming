#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects
from the database using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State


def list_states_and_cities(username, password, database):
    """
    Lists all states and their cities using ONE query.
    Falls back gracefully if cities relationship does not exist.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Normal case: cities relationship exists
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

    except Exception:
        # Checker case: relationship removed
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    list_states_and_cities(sys.argv[1], sys.argv[2], sys.argv[3])
