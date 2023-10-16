#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_instance_creation(self):
        """
        Test instance creation and attributes of the State class.
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_to_dict_method(self):
        """
        Test the to_dict method of the State class.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertTrue('to_dict' not in dir(state))
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "")
        self.assertEqual(state_dict['id'], state.id)

    def test_str_method(self):
        """
        Test the __str__ method of the State class.
        """
        state = State()
        string = str(state)
        self.assertIsInstance(string, str)
        self.assertIn("[State]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)
        self.assertIn("'name':", string)


if __name__ == '__main__':
    unittest.main()
