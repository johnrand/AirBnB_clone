#!/usr/bin/python3
""" this Module represents FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """example1 : for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return1: returns the dictionary __objects stored"""
        return FileStorage.__objects

    def new(self, obj):
        """example2: sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """example3: converts to the JSON file (path: __file_path)"""
        json_dict = dict()
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_dict))

    def classes(self):
        """return2: Returns a dictionary of valid classes & it references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.city import City


        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Place": Place,
                   "City": City,
                   "Amenity": Amenity,
                   "State": State,
                   "Review": Review}
        return classes

    def reload(self):
        """example4: will Reloads stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict_temp = obj_dict.copy()
            obj_dict = {}
            while obj_dict_temp:
                k, v = obj_dict_temp.popitem()
                obj_dict[k] = self.classes()[v["__class__"]](**v)
            FileStorage.__objects = obj_dict

    def attributes(self):
        """return3: valid attributes and it types for classname"""
        attributes = {
            "BaseModel": {
                "id": str,
                "updated_at": datetime.datetime,
                "created_at": datetime.datetime,
            },
            "User": {
                "last_name": str,
                "first_name": str,
                "password": str,
                "email": str,
            },
            "State": {"name": str},
            "Amenity": {"name": str},
            "City": {"state_id": str, "name": str},
            "Place": {
                "user_id": str,
                "amenity_ids": list,
                "name": str,
                "description": str,
                "max_guest": int,
                "number_rooms": int,
                "number_bathrooms": int,
                "price_by_night": int,
                "city_id": str,
                "latitude": float,
                "longitude": float,
            },
            "Review": {"user_id": str, "place_id": str, "user_id": str, "text": str},
        }
        return attributes
