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

database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                (user, password, host, database),
                pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        """
        _dict = {}
        if cls is None:
            _obj = []
            classes = ['User', 'State', 'City', 'Place', 'Review', 'Amenity']
            for _class in classes:
                result = self.__session.query(eval(_class))
                for res in result:
                    _obj.append(res)
        else:
            _obj = self.__session.query(cls).all()
        for obj in _obj:
            key = obj.__class__.__name__ + "." + str(obj.id)
            _dict[key] = obj
        return _dict

    def new(self, obj):
        """
        """
        if obj:
            self.__session.add()

    def save(self):
        """
        """
        if obj:
            self.__session.commit()

    def delete(self, obj=None):
        """
        """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
