#!/usr/bin/python3
"""This module contains the properties a Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for represents the  place objects"""

    city_id = ""
    user_id = ""
    name = ""
    latitude = 0.0
    longitude = 0.0
    number_bathrooms = 0
    max_guest = 0
    description = ""
    number_rooms = 0
    price_by_night = 0
    amenity_ids = []
