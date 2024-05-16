#!/usr/bin/python3
"""Base class module"""


import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Initialises the base class"""

        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = str(id)
        if created_at is None:
            self.created_at = str(datetime.now())
        else:
            self.created_at = created_at
        if updated_at is None:
            self.updated_at = str(datetime.now())
        else:
            self.updated_at = updated_at

    def save(self):
        """Updates the instance attribute (updated_at)
        with current datetime"""
        self.updated_at = str(datetime.now())
        """return self.updated_at"""

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dict__
        of the instance"""
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
