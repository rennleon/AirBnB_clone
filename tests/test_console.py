#!/usr/bin/python3
"""
This module containes test cases in the console
"""
import sys
import os
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Test cases class for Console"""

    def test_prompt(self):
        """ Test for the name in the prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)

    def test_command_empty_line(self):
        """Test for the empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual("", f.getvalue())

    def test_commnad_quit(self):
        """Test for command quit in the console"""
        self.assertTrue(HBNBCommand().onecmd('quit'))

    def test_command_EOF(self):
        """Test for command EOF in the console"""
        self.assertTrue(HBNBCommand().onecmd('EOF'))

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
