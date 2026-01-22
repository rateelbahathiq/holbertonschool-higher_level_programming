#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, database):
    """
    Connects to the database and prints the first State
    ordered by State.id.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
