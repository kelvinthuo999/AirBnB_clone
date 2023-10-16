#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test the City class.
    """

    def test_city_inherits_from_base_model(self):
        """
        Test that City inherits from BaseModel.
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """
        Test City attributes.
        """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_attribute_types(self):
        """
        Test data types of City attributes.
        """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_attributes_default(self):
        """
        Test that attributes are initialized as empty strings.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
