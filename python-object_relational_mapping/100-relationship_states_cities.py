#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
using SQLAlchemy ORM relationships.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_and_city(username, password, database):
    """
    Connects to the database and creates a State with
    an associated City using ORM relationships.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco")

    california.cities.append(san_francisco)

    session.add(california)
    session.commit()

    session.close()


if __name__ == "__main__":
    create_state_and_city(sys.argv[1], sys.argv[2], sys.argv[3])
