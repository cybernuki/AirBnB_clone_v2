#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):