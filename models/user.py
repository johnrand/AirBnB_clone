#!/usr/bin/python3
"""The module contains the info  User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for presents the user objects"""

    first_name = ""
    last_name = ""
    password = ""
    email = ""
    
