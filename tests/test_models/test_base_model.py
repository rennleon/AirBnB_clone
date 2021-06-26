#!/usr/bin/env python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """" Test cases class """
    def test_time_fields(self):
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)
