#!/usr/bin/python3
"""
unittest that tests the console for the AirBnB website
"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import unittest


class TestConsole(unittest.TestCase):
    """checks if all classes created correctly"""

    def TestClasses(self):
        self.assertEqual(City().__class__.__name__, "City")
        self.assertEqual(User().__class__.__name__, "User")
        self.assertEqual(State().__class__.__name__, "State")
        self.assertEqual(Amenity().__class__.__name__, "Amenity")
        self.assertEqual(Place().__class__.__name__, "Place")
        self.assertEqual(Review().__class__.__name__, "Review")

    def TestSubclassed(self):
        """Checks if the classes are subclassed correctly"""
        self.assertTrue(issubclass(User().__class__, BaseModel))
        self.assertTrue(issubclass(City().__class__, BaseModel))
        self.assertTrue(issubclass(State().__class__, BaseModel))
        self.assertTrue(issubclass(Amenity().__class__, BaseModel))
        self.assertTrue(issubclass(Place().__class__, BaseModel))
        self.assertTrue(issubclass(Review().__class__, BaseModel))

if __name__ == "__main__":
    unittest.main()
