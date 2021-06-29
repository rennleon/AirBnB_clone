#!/usr/bin/python3
"""
This module contains test cases for test_user.py
"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Test cases class for User"""

    def test_email(self):
        """Test for the email attribute"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """Test for password attribute"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """Test for first_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test for last_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
