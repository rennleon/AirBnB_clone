#!/usr/bin/python3
""""
This module defines City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines all common attributes/methods for City """
    state_id = ''
    name = ''
