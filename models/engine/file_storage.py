#!/usr/bin/python3
"""This is a file storage module"""


import json
import os


class FileStorage:
    """FileStorage class serializes instances to JSON file
    and deserializes JSON files to instances"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the object with key <obj class name>.id"""

        objKey = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[objKey] = obj

    def save(self):
        """serializes __objects to JSON file (path: __file_path)"""

        """obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                existing_objects = json.load(file)
        else:
            existing_objects = {}
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        all_objects = {**existing_objects, **obj_dict}
        with open(self.__file_path, 'w') as file:
            json.dump(all_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects
        Only if the JSON file (__file_path) exists
        Otherwise, do nothing
        if file does not exist, no execption is raised"""

        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = globals().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
