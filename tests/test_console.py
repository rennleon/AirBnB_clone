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
            self.assertEqual("", f.getvalue().strip())

    def test_commnad_quit(self):
        """Test for command quit in the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('quit'))

    def test_command_EOF(self):
        """Test for command EOF in the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('EOF'))
