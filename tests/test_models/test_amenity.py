#!/usr/bin/python3
"""
    This module contains test cases for Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """"Test cases class for Amenity"""

    def test_name(self):
        """Test for name attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
