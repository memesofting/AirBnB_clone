#!/usr/bin/python3
"""This is a file storage module"""


class FileStorage:
    """FileStorage class serializes instances to JSON file
    and deserializes JSON files to instances"""
    
    __file_path = "storage.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary __objects"""
        pass
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        pass
    
    def save(self):
        """serializes __objects to JSON file (path: __file_path)"""
        pass
    
    def reload(self):
        """deserializes the JSON file to __objects
        Only if the JSON file (__file_path) exists
        Otherwise, do nothing
        if file does not exist, no execption is raised"""
        pass
