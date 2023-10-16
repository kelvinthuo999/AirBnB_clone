#!/usr/bin/python3
""" unit test for BaseModel class """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    # Add module-level documentation
    """
    This is a unit test module for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of a BaseModel instance.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Verify that the id is a non-empty string
        self.assertIsInstance(model.id, str)
        self.assertNotEqual(model.id, "")
        # Verify that created_at and updated_at are datetime objects
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        # Verify that the instance is added to the storage
        self.assertIn(model, models.storage.all().values())

    def test_str(self):
        """
        Test the __str__ method of a BaseModel instance.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Verify that the string representation is in the expected format
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """
        Test the save method of a BaseModel instance.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Get the initial updated_at timestamp
        initial_updated_at = model.updated_at
        # Update the instance
        model.save()
        # Get the updated updated_at timestamp
        updated_updated_at = model.updated_at
        # Verify that updated_at is changed after calling save
        self.assertNotEqual(initial_updated_at, updated_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of a BaseModel instance.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Convert the instance to a dictionary
        model_dict = model.to_dict()
        # Verify the dictionary contains the expected keys
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)


if __name__ == '__main__':
    unittest.main()
