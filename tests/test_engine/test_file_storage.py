import unittest

class TestFileStorage(unittest.TestCase):
    def test_empty_dictionary(self):
        storage = FileStorage()
        assert storage.all() == {}
        
    def test_objects_none(self):
        storage = FileStorage()
        storage._FileStorage__objects = None
        assert storage.all() is None
