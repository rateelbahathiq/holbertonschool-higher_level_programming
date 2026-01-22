#!/usr/bin/python3
"""
Changes the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, database):
    """
    Connects to the database and updates the State
    with id = 2 to have the name 'New Mexico'.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
