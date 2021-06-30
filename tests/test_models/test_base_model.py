#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
import pep8
from uuid import uuid4
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """" Test cases class for Base Model """

    def setUp(self) -> None:
        """ Setup function to append the objects to the test """
        super().setUp()
        self.obj = BaseModel()
        self.obj2 = BaseModel()

    def test_pep8_base_model(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_unique_id(self):
        """ Test the creation of unique id's for each instance """
        obj1 = BaseModel()
        sleep(0.01)
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_attr_types(self):
        """ Test the types of the default attrs of a BaseModel instance """
        self.assertIs(type(self.obj.id), str)
        self.assertIs(type(self.obj.created_at), datetime)
        self.assertIs(type(self.obj.updated_at), datetime)

    def test_time_attrs(self):
        """ Test for BaseModel time fields """
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertLess(self.obj.created_at, self.obj2.created_at)

    def test__str__method(self):
        """ Test __str__ method """
        str_rep = "[{}] ({}) {}"\
            .format(self.obj.__class__.__name__,
                    self.obj.id, self.obj.__dict__)
        self.assertEqual(self.obj.__str__(), str_rep)

    def test_to_dict_method(self):
        """ Test to_dict method """
        from_dict = self.obj.__dict__
        from_to_dict = self.obj.to_dict()

        self.assertIs(type(from_to_dict), dict)
        self.assertEqual(BaseModel.__name__, from_to_dict['__class__'])
        self.assertEqual(from_dict['id'], from_to_dict['id'])

    def test_to_dict_method_with_one_param(self):
        """ test to_dict method with one param """
        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(None)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict([])
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict({})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(True)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(False)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(dict())
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict({'id': 123, 'created_at': datetime.now()})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict('Ranmod value')

    def test_save_method(self):
        """ Test save method """
        objid = self.obj.id
        self.assertEqual(self.obj.id, objid)
        self.assertEqual(self.obj.created_at, self.obj.updated_at)

        sleep(0.01)
        self.obj.save()

        self.assertEqual(self.obj.id, objid)
        self.assertNotEqual(self.obj.created_at, self.obj.updated_at)
        self.assertLess(self.obj.created_at, self.obj.updated_at)

    def test_save_method_with_one_param(self):
        """ Test save method by passing one param """
        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save(None)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save([])
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save({})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save(True)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save(False)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save(dict())
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save({'id': 123, 'created_at': datetime.now()})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save('Ranmod value')

    def test_create_BaseModel_from_dictionary_as_kwargs(self):
        """ Test for BaseModel instance creation using kwargs """
        id = str(uuid4())
        now = datetime.now().isoformat()
        my_dict = {
            'id': id,
            'name': 'Jhon Smith',
            'created_at': now,
            'updated_at': now
        }
        obj1 = BaseModel(**my_dict)

        self.assertEqual(obj1.id, id)
        self.assertEqual(obj1.name, 'Jhon Smith')
        self.assertEqual(now, obj1.created_at.isoformat())
        self.assertEqual(now, obj1.updated_at.isoformat())

    def test_create_BaseModel_from_dictionary_as_kwargs_valid_attrs(self):
        """ Test cases for instantiation from kwargs """
        id = str(uuid4())
        now = datetime.now().isoformat()
        my_dict = {
            'id': id,
            '__class__': 'dict',
            'created_at': now,
            'updated_at': now
        }
        obj1 = BaseModel(**my_dict)

        self.assertEqual(obj1.id, id)
        self.assertIs(obj1.__class__, BaseModel)
        self.assertEqual(now, obj1.created_at.isoformat())
        self.assertEqual(now, obj1.updated_at.isoformat())

    def test_create_BaseModel_from_dictionary_as_kwargs_empty(self):
        """ Test for BaseModel instance creation using empty kwargs """
        empty_dict = dict()
        obj1 = BaseModel(**empty_dict)

        self.assertIs(type(obj1), BaseModel)
        self.assertIs(type(obj1.id), str)
        self.assertIs(type(obj1.created_at), datetime)
        self.assertIs(type(obj1.updated_at), datetime)

    def test_create_BaseModel_from_dictionary_as_kwargs_diff_fields(self):
        """ Test for BaseModel instance creation using kwargs """
        my_dict = {
            'name': 'Jhon Smith',
            'age': 34
        }

        obj = BaseModel(**my_dict)

        self.assertEqual(obj.name, 'Jhon Smith')
        self.assertEqual(obj.age, 34)

        regex = "object has no attribute 'id'"
        with self.assertRaisesRegex(AttributeError, regex):
            obj.id

        regex = "object has no attribute 'created_at'"
        with self.assertRaisesRegex(AttributeError, regex):
            obj.created_at

        regex = "object has no attribute 'updated_at'"
        with self.assertRaisesRegex(AttributeError, regex):
            obj.updated_at

    def test_create_BaseModel_from_dictionary_as_kwargs_wrong_format(self):
        """ Test for BaseModel instance creation wrong kwargs types """
        id = uuid4()
        now = datetime.now()
        my_dict = {
            'id': id,
            'name': 'Jhon Smith',
            'created_at': now,
            'updated_at': now
        }

        regex = 'must be str, not datetime.datetime'
        with self.assertRaisesRegex(TypeError, regex):
            BaseModel(**my_dict)

    def test_create_BaseModel_from_args(self):
        """ Test for BaseModel instance creation using args """
        args = [True, 'Random', 34.2]
        obj = BaseModel(*args)

        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_create_new_attrs(self):
        """ Test for BaseModel attrs creation """
        self.obj.name = 'Jhon'
        self.obj.age = 46

        self.assertEqual(self.obj.name, 'Jhon')
        self.assertEqual(self.obj.age, 46)
