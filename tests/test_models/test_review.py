#!/usr/bin/python3
"""
    This module contains test cases for Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """" Test cases class for Review"""

    def test_place_id(self):
        """Test for place_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """Test for user_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_text(self):
        """Test for text attribute"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
