#!/usr/bin/python3
"""
Defines the State class mapped to the states table,
with a relationship to the City class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class mapped to the states table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship to City with cascade delete
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete"
    )
