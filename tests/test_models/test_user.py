#!/usr/bin/python3
"""
Unit tests for the User class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_instance_creation(self):
        """
        Test instance creation and attributes of the User class.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict_method(self):
        """
        Test the to_dict method of the User class.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue('to_dict' not in dir(user))
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertEqual(user_dict['id'], user.id)

    def test_str_method(self):
        """
        Test the __str__ method of the User class.
        """
        user = User()
        string = str(user)
        self.assertIsInstance(string, str)
        self.assertIn("[User]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)
        self.assertIn("'email':", string)
        self.assertIn("'password':", string)
        self.assertIn("'first_name':", string)
        self.assertIn("'last_name':", string)

if __name__ == '__main__':
    unittest.main()
