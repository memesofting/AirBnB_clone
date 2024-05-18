#!/usr/bin/python3
"""Base class module"""


from typing import Any
import uuid
from datetime import datetime
'''from models.__init__ import storage'''


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialises the base class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                '''if key is not '__class__':'''
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))

    def save(self):
        """Updates the instance attribute (updated_at)
        with current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()
        """return self.updated_at"""

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dict__
        of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = str(self.created_at)
        dict_copy['updated_at'] = str(self.updated_at)
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

    def to_obj(self, **kwargs):
        """returns object from dictionary representation"""
        pass

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def __setattr__(self, attr_name, value):
        """updates 'update_at' whenever an objects is modified
        by overriding __setattr__"""
        if attr_name == "updated_at":
            self.__dict__[attr_name] == datetime.now()
