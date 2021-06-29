#!/usr/bin/python3
""""
This module defines Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines all common attributes/methods for Review """
    place_id = ''
    user_id = ''
    text = ''
