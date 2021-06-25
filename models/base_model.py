#!/usr/bin/env python3

from uuid import uuid4
from datetime import datetime

class BaseModel():
    
    def __init__(self):
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.updated_at = self.create_at
        
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
        
    def save(self):
        self.updated_at = datetime.now()


