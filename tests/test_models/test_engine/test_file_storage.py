#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        objects = [
            BaseModel(),
            User(),
            State(),
            Place(),
            City(),
            Amenity(),
            Review()
        ]
        i = 0
        while i < len(objects):
            models.storage.new(objects[i])
            i += 1

        key_checks = [
            ("BaseModel." + objects[0].id, objects[0]),
            ("User." + objects[1].id, objects[1]),
            ("State." + objects[2].id, objects[2]),
            ("Place." + objects[3].id, objects[3]),
            ("City." + objects[4].id, objects[4]),
            ("Amenity." + objects[5].id, objects[5]),
            ("Review." + objects[6].id, objects[6])
        ]

        for key, value in key_checks:
            self.assertIn(key, models.storage.all().keys())
            self.assertIn(value, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        objects = [
            BaseModel(),
            User(),
            State(),
            Place(),
            City(),
            Amenity(),
            Review()
        ]
        i = 0
        while i < len(objects):
            models.storage.new(objects[i])
            i += 1

        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()

        key_checks = [
            ("BaseModel." + objects[0].id),
            ("User." + objects[1].id),
            ("State." + objects[2].id),
            ("Place." + objects[3].id),
            ("City." + objects[4].id),
            ("Amenity." + objects[5].id),
            ("Review." + objects[6].id)
        ]

        for key in key_checks:
            self.assertIn(key, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        objects = [
            BaseModel(),
            User(),
            State(),
            Place(),
            City(),
            Amenity(),
            Review()
        ]
        i = 0
        while i < len(objects):
            models.storage.new(objects[i])
            i += 1

        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects

        key_checks = [
            ("BaseModel." + objects[0].id),
            ("User." + objects[1].id),
            ("State." + objects[2].id),
            ("Place." + objects[3].id),
            ("City." + objects[4].id),
            ("Amenity." + objects[5].id),
            ("Review." + objects[6].id)
        ]

        for key in key_checks:
            self.assertIn(key, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
