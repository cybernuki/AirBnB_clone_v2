#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        _list = []
        for _id, city in models.storage.all(City).items():
            if self.id == city.state_id:
                _list.append(city)
        return _list
