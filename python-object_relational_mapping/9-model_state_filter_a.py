#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username, password, database):
    """
    Connects to the database and lists all State objects
    whose names contain the letter 'a', ordered by id.
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
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
