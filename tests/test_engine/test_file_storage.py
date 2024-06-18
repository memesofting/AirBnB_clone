import unittest
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage class"""

    def setUp(self):
        """sets up tests"""

        self.storage = FileStorage()
        self.my_model = BaseModel()
        self.my_model.name = "First_Model"
        self.my_model.my_number = 89
        self.storage.new(self.my_model)

    def tearDown(self):
        """cleans up test"""
        
        file_path = FileStorage._FileStorage__file_path
        print(f"TearDown: Attempting to remove the file at {file_path}")
        
        if os.path.exists(file_path):
            os.remove(file_path)
            print("File successfully removed.")
        else:
            print("No file found to remove.")
        del self.storage
        del self.my_model

    def test_new(self):
        """test the new method to ensure objects are added
        to __objects with correct key"""
        
        key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.my_model)

    def test_reload(self):
        """tests fro proper deserialisation from JSON file"""
        
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['name'], "First_Model")
        self.assertEqual(data[key]['my_number'], 89)
        pass

    def test_all(self):
        """test the all method to ensure that it returns all objects"""

        pass


if __name__ == '__main__':
    unittest.main()
