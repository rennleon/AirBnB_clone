#!/usr/bin/python3
"""
    This module contains test cases for FileStorage
"""
import unittest
from models import engine
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """" Test cases class """
    def setUp(self):
        super().setUp()
        self.storage = FileStorage()

    def test_method_all(self):
        empty_dict = dict()
        all = self.storage.all()

        self.assertDictEqual(empty_dict, all)
