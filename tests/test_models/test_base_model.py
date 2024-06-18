import unittest
import time
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        """sets up tests for basemodel"""

        self.my_model = BaseModel()
        self.storage = FileStorage()
        self.my_model_with_kwargs = BaseModel(
            id="1234", created_at="2024-06-17T13:14:07.751138",
            updated_at="2024-06-17T13:14:07.751205", name="Test")

    def tearDown(self):
        """cleans up test files for basemodel"""

        file_path = FileStorage._FileStorage__file_path
        if os.path.exists(file_path):
            os.remove(file_path)
        del self.my_model
        del self.my_model_with_kwargs

    def test_instance(self):
        """Test for the initialisation of the base model"""

        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_kwargs_initialisation(self):
        """Test for inilialisation of an object with kwargs"""
        pass

    def test_save(self):
        """Tests that the updated_at attribute is
        updated to the current time"""

        self.my_model = BaseModel()
        old_time = self.my_model.updated_at
        time.sleep(0.1)
        self.my_model.save()
        new_time = self.my_model.updated_at
        self.assertNotEqual(new_time, old_time)

    def test_str_method(self):
        """Test the __str__ method for correct output"""

        model_str = self.my_model
        expected_str = f"[BaseModel] ({model_str.id}) {model_str.__dict__}"
        self.assertEqual(str(model_str), expected_str)

    def test_setattr_updates_updated_at(self):
        """Test that setting an attribute updates `updated_at`"""

        model = BaseModel()
        old_time = model.created_at
        time.sleep(0.1)  # Ensure the time changes
        model.name = "test"
        new_time = model.updated_at
        self.assertNotEqual(new_time, old_time)
        self.assertTrue(new_time, old_time)
        self.assertEqual(model.name, "test")

    def test_to_dict_method(self):
        """Test the to_dict method creates
        accurate dictionary representation"""

        create_time = str(self.my_model.created_at)
        update_time = str(self.my_model.updated_at)
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict['id'], self.my_model.id)
        self.assertEqual(model_dict['created_at'], create_time)
        self.assertEqual(model_dict['updated_at'], update_time)
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
