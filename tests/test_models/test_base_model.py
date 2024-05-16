import unittest

from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_instance(self):
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model, BaseModel))

    def test_save(self):
        """Tests that the updated_at attributeis
        updated to the current time"""

        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(str(base_model.updated_at), str(datetime.now()))
    
    """test for empty kwargs"""

if __name__ == "__main__":
    unittest.main()
