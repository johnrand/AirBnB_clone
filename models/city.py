#!/usr/bin/python3
"""This module contains the definition of
the city class for a User"""

from models.base_model import BaseModel


class City(BaseModel):
    """A Class that represents city objects"""

    state_id = ""
    name = ""
