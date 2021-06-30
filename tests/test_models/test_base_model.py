#!/usr/bin/python3
"""Test BaseModel- Comproving expectect outputs and documentation"""
from datetime import datetime
import time
import unittest
# from pep8 import pycodestyle
import models
import inspect
from unittest import mock

BaseModel = models.base_model.BaseModel
mod_doc = models.base_model.__doc__

class TestBaseModel(unittest.TestCase):
    """testing BaseModel Class"""

    def test_save_method(self):
        """test save method and if it updates
        "updated_at" calling storage.save"""
        instance4 = BaseModel()
        created_at = instance4.created_at
        updated_at = instance4.updated_at
        instance4.save()
        new_created_at = instance4.created_at
        new_updated_at = instance4.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
