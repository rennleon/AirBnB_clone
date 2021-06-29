#!/usr/bin/python3
"""
    This module contains test cases for City
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """" Test cases class for City"""

    def test_state_id(self):
        """Test for place_id attribute"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """Test for name attribute"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
