import unittest
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        self.my_model = BaseModel()

    def tearDown(self):
        del self.my_model

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
