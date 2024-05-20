import unittest
"""from models.base_model import BaseModel"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage class"""
    
    def test_empty_dictionary(self):
        storage = FileStorage()
        assert storage.all() == {}

    def test_objects_none(self):
        storage = FileStorage()
        storage._FileStorage__objects = None
        assert storage.all() is None

    def test_object_creation(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertIsInstance(my_model, BaseModel)


if __name__ == '__main__':
    unittest.main()
