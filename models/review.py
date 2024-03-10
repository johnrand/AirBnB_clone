#!/usr/bin/python3
"""This module contains information for  Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for represents review objects"""

    place_id = ""
    text = ""
    user_id = ""
