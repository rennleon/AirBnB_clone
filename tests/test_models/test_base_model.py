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
    # def test_dictionary(self):
    #     """testing to_dict correct funtionality"""
    #     instance3 = BaseModel()
    #     instance3.name = "Holbies"
    #     instance3.my_number = 89
    #     new_inst = instance3.to_dict()
    #     expectec_attrs = ["id",
    #                       "created_at",
    #                       "updated_at",
    #                       "name",
    #                       "my_number",
    #                       "__class__"]
    #     self.assertCountEqual(new_inst.keys(), expectec_attrs)
    #     self.assertEqual(new_inst['__class__'], 'BaseModel')
    #     self.assertEqual(new_inst['name'], 'Holbies')
    #     self.assertEqual(new_inst['my_number'], 89)

    def test_str_method(self):
        """testing str method, checking output"""
        instance4 = BaseModel()
        strr = "[BaseModel] ({}) {}".format(instance4.id, instance4.__dict__)
        self.assertEqual(strr, str(instance4))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
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
        self.assertTrue(mock_storage.save.called)
