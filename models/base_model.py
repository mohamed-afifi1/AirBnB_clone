#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime


class BaseModel:
    """This is the base model"""
    def __init__(self, *args, **kwargs):
        """This is the init method"""

        if kwargs is None or kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k in kwargs.keys():
                if k != "__class__":
                    if k == "id":
                        self.__dict__[k] = kwargs[k]
                    elif k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(
                            kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[k] = kwargs[k]

    def __str__(self):
        """This is the str method"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This is the save method"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """This is the to_dict method"""

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
