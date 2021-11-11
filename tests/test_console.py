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
import pep8


class TestConsole(unittest.TestCase):
    """checks if all classes created and pep8"""

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

    def pep8_base_model(self):
        """pep8 confirmance for BaseModel class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

    def pep8_user(self):
        """pep8 confirmance for User class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/user.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

    def pep8_city(self):
        """pep8 confirmance for City class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

    def pep8_state(self):
        """pep8 confirmance for State class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/state.py'])
        self.assertEqual(res.total_errors, 0, "Code Style errors")

    def pep8_amenity(self):
        """pep8 confirmance for Amenity class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

    def pep8_place(self):
        """pep8 confirmance for Place class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

    def pep8_review(self):
        """pep8 confirmance for Review class"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/review.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

    def pep8_init(self):
        """pep8 confirmance for __init__"""
        pep = pep8.StyleGuide(quit=True)
        res = pep.check_files(['models/__init__.py'])
        self.assertEqual(res.total_errors, 0, "Code style errors")

if __name__ == "__main__":
    unittest.main()
