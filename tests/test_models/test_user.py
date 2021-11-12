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

if __name__ == '__main__':
    unittest.main()
