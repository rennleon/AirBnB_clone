#!/usr/bin/python3
"""
    This module contains test cases for State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """" Test cases class for State"""

    def test_name(self):
        """Test for the name attribute"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
