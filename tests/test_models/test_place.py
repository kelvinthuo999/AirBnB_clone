#!/usr/bin/python3
"""
Unit tests for the Place class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Defines the test cases for the Place class.
    """

    def test_inheritance(self):
        """
        Test if Place inherits from BaseModel.
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the Place class.
        """
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_attributes_defaults(self):
        """
        Test if attributes have the correct default values.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str(self):
        """
        Test the __str__ method of Place.
        """
        place = Place()
        place_id = place.id
        place_str = place.__str__()
        expected = "[Place] ({}) {}".format(place_id, place.__dict__)
        self.assertEqual(place_str, expected)

    def test_to_dict(self):
        """
        Test the to_dict method of Place.
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], place.id)
        self.assertEqual(place_dict['created_at'], place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], place.updated_at.isoformat())

    def test_to_dict_attrs(self):
        """
        Test if the 'to_dict' method includes all required attributes.
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertTrue('city_id' in place_dict)
        self.assertTrue('user_id' in place_dict)
        self.assertTrue('name' in place_dict)
        self.assertTrue('description' in place_dict)
        self.assertTrue('number_rooms' in place_dict)
        self.assertTrue('number_bathrooms' in place_dict)
        self.assertTrue('max_guest' in place_dict)
        self.assertTrue('price_by_night' in place_dict)
        self.assertTrue('latitude' in place_dict)
        self.assertTrue('longitude' in place_dict)
        self.assertTrue('amenity_ids' in place_dict)

if __name__ == '__main__':
    unittest.main()
