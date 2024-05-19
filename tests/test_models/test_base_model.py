import unittest
import uuid
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_instance(self):
        """Test for the initialisation of the base model"""

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model, BaseModel))
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test_kwargs_initialisation(self):
        """Test for inilialisation of an object with kwargs"""
        pass

    def test_save(self):
        """Tests that the updated_at attribute is
        updated to the current time"""

        base_model = BaseModel()
        old_time = base_model.updated_at
        time.sleep(0.1)
        base_model.save()
        new_time = base_model.updated_at
        self.assertNotEqual(new_time, old_time)

    def test_str_method(self):
        """Test the __str__ method for correct output"""

        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)

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

        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], str(model.created_at))
        self.assertEqual(model_dict['updated_at'], str(model.updated_at))
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
