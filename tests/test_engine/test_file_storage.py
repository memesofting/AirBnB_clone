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

    def tearDown(self):
        """cleans up test"""

        del self.storage
        del self.my_model

    def test_new(self):
        """test the new method to ensure objects are added
        to __objects with correct key"""

        pass

    def test_reload(self):
        """tests fro proper deserialisation from JSON file"""

        pass

    def test_all(self):
        """test the all method to ensure that it returns all objects"""

        pass


if __name__ == '__main__':
    unittest.main()
