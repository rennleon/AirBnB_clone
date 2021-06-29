#!/usr/bin/python3
"""
    This module contains test cases for FileStorage
"""
import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """" Test cases class for FileStorage """
    def setUp(self) -> None:
        super().setUp()
        self.file_path = 'file.json'

    def test_instance_creation(self):
        """ Test for FfileStorage instance creation """
        my_storage = FileStorage()
        self.assertIs(type(my_storage), FileStorage)