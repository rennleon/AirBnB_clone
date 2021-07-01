#!/usr/bin/python3
"""
This module containes test cases in the console
"""
import unittest
import os
from models.base_model import BaseModel
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Test cases class for Console"""

    def test_prompt(self):
        """ Test for the name in the prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)

    def test_commnad_quit(self):
        """Test for command quit in the console"""
        self.assertTrue(HBNBCommand().onecmd('quit'))

    def test_command_EOF(self):
        """Test for command EOF in the console"""
        self.assertTrue(HBNBCommand().onecmd('EOF'))


class test_other_classes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_command_empty_line(self):
        """Test for the empty line"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertEqual("", output.getvalue().strip())

    def test_command_classes(self):
        """Checks he classes in the console"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
            HBNBCommand().onecmd('.all()')
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())


class test_command_all(unittest.TestCase):
    """Test for command all in the console"""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_commad_all(self):
        """Test for command all in the console"""
        msg = '** class doesn\'t exist **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('all MyModel'))
            self.assertEqual(msg, output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('MyModel.all()'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_command_all_advance(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())


class test_command_help(unittest.TestCase):
    """Test for command help in the console"""

    def test_command_help_EOF(self):
        """Test for command help 'EOF' in the console"""
        com_h = 'Quit command to exit the program'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help EOF'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_quit(self):
        """Test for command help 'quit' in the console"""
        com_h = 'Quit command to exit the program'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help quit'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help(self):
        """Test for command help in the console"""
        com_h = ('Documented commands (type help <topic>):' +
                 '\n========================================' +
                 '\nEOF  all  count  create  destroy  help' +
                 '  quit  show  update')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_all(self):
        """Test for command help 'all' in the console"""
        com_h = 'Prints all string representation of all instances'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help all'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_count(self):
        """Test for command help 'count' in the console"""
        com_h = ('Retrieves the number of instances of a class' +
                 ': <class name>.count().')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help count'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_create(self):
        """Test for command help 'create' in the console"""
        com_h = ("Creates a new instance of BaseModel, " +
                 "saves it to a JSON file" +
                 "\n        and prints the 'id'")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help create'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_destroy(self):
        """Test for command help 'destroy' in the console"""
        com_h = 'Deletes an instance based on the class name and id'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help destroy'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_show(self):
        """Test for command help 'show' in the console"""
        com_h = ('Prints the string representation of an instance' +
                 '\n        based on the class name and id')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help show'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_command_help_update(self):
        """Test for command help 'update' in the console"""
        com_h = ('Updates an instance based on the class name' +
                 '\n        and id by adding or updating an attribute' +
                 '\n        Usage: update <class name> <id> <attribute name>' +
                 '\n        "<attribute value>"')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help update'))
            self.assertEqual(com_h, output.getvalue().strip())


class test_command_create(unittest.TestCase):
    """Test for command create in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_create_name_missing(self):
        """Test for command create with class name missing """
        msg = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_name_exist(self):
        """Test for command create with class invalid"""
        msg = '** class doesn\'t exist **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create MyModel'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_id(self):
        """test for command create with 'id' """
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id1 = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id2 = output.getvalue().strip()
            self.assertNotEqual(test_id1, test_id2)


class test_command_show(unittest.TestCase):
    """Test for command show in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_show_name_missing(self):
        """Test for command show with class name missing"""
        msg = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_name_exist(self):
        """Test for command show with class invalid"""
        msg = '** class doesn\'t exist **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show MyModel'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_id_missing(self):
        """Test for command show with id missing"""
        msg = '** instance id missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_id(self):
        """Test for command show with 'id' """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create User')
            test_id = output.getvalue().strip()
            parameter_1 = 'show User {}'.format(test_id)
            parameter_2 = 'User.show ("{}")'.format(test_id)
            comm_show1 = HBNBCommand().onecmd(parameter_1)
            comm_show2 = HBNBCommand().onecmd(parameter_2)
            self.assertEqual(comm_show1, comm_show2)

    def test_show_invalid_id(self):
        """Test for command show with invalid id """
        msg = '** no instance found **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel 34'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_more_than_one_arg(self):
        """Test for command show with invalid id """
        msg = '** no instance found **'
        parameter_1 = 'show BaseModel 34 other attr'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(parameter_1))
            self.assertEqual(msg, output.getvalue().strip())
