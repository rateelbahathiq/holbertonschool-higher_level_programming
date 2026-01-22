#!/usr/bin/python3
"""
Prints the id of the State object with the given name
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_id(username, password, database, state_name):
    """
    Connects to the database and prints the id of the State
    matching the given name, or 'Not found' if it doesn't exist.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()


if __name__ == "__main__":
    get_state_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
