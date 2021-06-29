#!/usr/bin/python3
"""
    This module contains test cases for Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """" Test cases class for Place"""
     
    def test_city_id(self):
        """Test for the city_id attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """Test for the user_id attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name(self):
        """Test for the name attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
    
    def test_description(self):
        """Test for the description attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """Test for the numbers_rooms attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertIsInstance(place.number_rooms, int)

    def test_number_bathrooms(self):
        """Test for the number_bathrooms attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertIsInstance(place.number_bathrooms, int)

    def test_max_guest(self):
        """Test for the max_guest attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertIsInstance(place.max_guest, int)
    
    def test_price_by_night(self):
        """Test for the price_by_night attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertIsInstance(place.price_by_night, int)

    def test_latitude(self):
        """Test for the latitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertIsInstance(place.latitude, float)
    
    def test_longitude(self):
        """Test for the longitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertIsInstance(place.longitude, float)

    def test_amenity_ids(self):
        """Test for the amenity_ids attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertIsInstance(place.amenity_ids, list)