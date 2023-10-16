#!/usr/bin/python3
"""Unit tests for the `amenity` module.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_instantiation(self):
        """
        Test that an instance of Amenity is correctly instantiated.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """
        Test that Amenity has the expected attributes.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """
        Test the to_dict method of Amenity.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('name', amenity_dict)


if __name__ == '__main__':
    unittest.main()
