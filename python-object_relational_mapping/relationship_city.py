#!/usr/bin/python3
"""
Defines the City class mapped to the cities table,
with a relationship to the State class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City class mapped to the cities table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Reference to the State object
    state = relationship("State", back_populates="cities")
