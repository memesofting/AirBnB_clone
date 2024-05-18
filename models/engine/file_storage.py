#!/usr/bin/python3
"""This is a file storage module"""


import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class serializes instances to JSON file
    and deserializes JSON files to instances"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        objKey = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[objKey] = obj

    def save(self):
        """serializes __objects to JSON file (path: __file_path)"""
        for key, obj in self.__objects.items():
            obj_dict = {key: obj.to_dict()}
        with open(self.__filepath, 'w') as file:
            json.dump(self.obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        Only if the JSON file (__file_path) exists
        Otherwise, do nothing
        if file does not exist, no execption is raised"""
        if self.__file_path:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    className = value['__class__']
