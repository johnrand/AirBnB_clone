#!/usr/bin/python3
"""makes the BaseModel class."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel is a base class for all other models."""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of the BaseModel class.
        """

        if kwargs:
            iterator = iter(kwargs.items())
            while True:
                try:
                    key, value = next(iterator)
                    if key == "created_at":
                        self.__dict__["created_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    elif key == "updated_at":
                        self.__dict__["updated_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
                except StopIteration:
                    break
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        It Update public instance attribute updated_at
        with current datetime and  BaseModel instance
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """it Updates the public instance attribute 'updated_at'
        with the current datetime and saves the BaseModel instance."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return1: Returns a dictionary that containing all
        keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
