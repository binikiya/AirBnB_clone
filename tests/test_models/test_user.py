#!/usr/bin/python3
"""
Unittest class for models/user.py
"""
from models.user import User
import unittest
from datetime import datetime
from time import sleep
import os
import models


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestUser(unittest.TestCase):
    """unittest for User class instantiation"""

    def test_with_no_args_instatiates(self):
        """tests with no argument"""
        self.assertEqual(User, type(User()))

    def test_with_new_stored_instances(self):
        """tests with new stored instances"""
        self.assertIn(User(), models.storage.all().values())

    def test_if_id_is_public(self):
        """tests that if id is public string"""
        self.assertEqual(str, type(User().id))

    def test_if_created_at_is_public(self):
        """tests that if created_at is public datetime"""
        self.assertEqual(datetime, type(User().created_at))

    def test_if_updated_at_is_public(self):
        """tests that if updated_at is public datetime"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_if_email_is_public(self):
        """tests that if email is public string"""
        self.assertEqual(str, type(User().email))

    def test_if_password_is_public(self):
        """test that if password is public string"""
        self.assertEqual(str, type(User().password))

    def test_if_first_name_is_public(self):
        """test that if first_name is public string"""
        self.assertEqual(str, type(User().first_name))

    def test_if_last_name_is_public(self):
        """test that if last_name is public string"""
        self.assertEqual(str, type(User().last_name))

    def test_with_two_unique_users_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_with_different_created_at(self):
        user1 = User()
        sleep(0.5)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_with_different_updated_at(self):
        user1 = User()
        sleep(0.5)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_repr(self):
        user = User()
        user.id = "123456"
        date = datetime.today()
        date_repr = repr(date)
        user.created_at = user.updated_at = date
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + date_repr, user_str)
        self.assertIn("'updated_at': " + date_repr, user_str)

    def test_with_unsed_args(self):
        self.assertNotIn(None, User(None).__dict__.values())

    def test_with_kwargs_instatiation(self):
        date = datetime.today()
        date_iso = date.isoformat()
        user = User(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user.id, "123")
        self.assertEqual(user.created_at, date)
        self.assertEqual(user.updated_at, date)

    def test_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

class TestUserSave(unittest.TestCase):
    """Testing save method in the User class"""

    @classmethod
    def SetUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def RenameRemove(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user = User()
        sleep(0.5)
        up_at = user.updated_at
        user.save()
        self.assertLess(up_at, user.updated_at)

    def test_two_save(self):
        user = User()
        sleep(0.5)
        up_at1 = user.updated_at
        user.save()
        self.assertLess(up_at1, user.updated_at)
        up_at2 = user.updated_at
        sleep(0.5)
        user.save()
        self.assertLess(up_at2, user.updated_at)

    def test_with_none_arg(self):
        with self.assertRaises(TypeError):
            User().save(None)

    def test_save_if_updates(self):
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())

class TestUserDict(unittest.TestCase):
    """unittest for testing to_dict mothod of User class"""

    def test_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_dict_with_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_dict_with_added_attr(self):
        user = User()
        user.middle_name = "ALX"
        user.my_number = 88
        self.assertEqual("ALX", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_if_datetime_attr(self):
        user_dict = User().to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = date
        dict_t = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), dict_t)

    def test_with_dict(self):
        self.assertNotEqual(User().to_dict(), User().__dict__)

    def test_with_none_args(self):
        with self.assertRaises(TypeError):
            User().to_dict(None)

if __name__ == '__main__':
    unittest.main()
