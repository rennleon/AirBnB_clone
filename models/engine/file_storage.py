#!/usr/bin/env python3
"""" Definition of FileStorage class """

import json
from uuid import uuid4
from datetime import datetime
from os import path


class FileStorage():
    """ FileStorage class """
    __file_path = 'objects.json'
    __objects = dict()

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in '__objects' the 'obj' with key '<obj class_name>.id' """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes '__objects' to into JSON file (path: '__file_path') """

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """ Deserializes a JSON file to '__objects'
        only if '__file_path' exists """
        if not path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
            FileStorage.__objects = json.load(file)
