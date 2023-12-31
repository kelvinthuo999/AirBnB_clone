#!/usr/bin/python3
"""
Unittests for the Review class.
"""
from datetime import datetime
import inspect
from models.review import Review
from models.base_model import BaseModel
import pep8
import unittest


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_inheritance(self):
        """
        Test inheritance of Review class.
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """
        Test attributes of Review class.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attribute_types(self):
        """
        Test attribute types of Review class.
        """
        review = Review()
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)


if __name__ == '__main__':
    unittest.main()
