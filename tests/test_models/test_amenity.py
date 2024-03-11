#!/usr/bin/python3
"""makes unittests for all models/amenity.py.

Unittest classes:
    TestAmenityinstantiation
    TestAmenitysave
    TestAmenitytodict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests testing the Amenity class."""

    def test_noargs(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_uniqueids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_createdat(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_updatedat(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_through_kwargs(self):
        """instantiation through kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_through_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests  testing  methods for the Amenity class."""

    def test_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_correct_keys(self):
        am = Amenity()
        keys_to_check = ["id", "created_at", "updated_at", "__class__"]
        am_dict = am.to_dict()
        i = 0
        while i < len(keys_to_check):
            self.assertIn(keys_to_check[i], am_dict)
            i += 1

    def test_to_added_attributes(self):
        am = Amenity()
        am.middle_name = "My_First_Model"
        am.my_number = 89
        self.assertEqual("My_First_Model", am.middle_name)
        am_dict = am.to_dict()
        self.assertIn("my_number", am_dict)

    def test_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        keys_to_check = ["id", "created_at", "updated_at"]
        i = 0
        while i < len(keys_to_check):
            self.assertEqual(str, type(am_dict[keys_to_check[i]]))
            i += 1
    
    def test_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), expected_dict)

    def test_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_through_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


class TestAmenitysave(unittest.TestCase):
    """Unittests testing save method for Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_through_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updatesfile(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


if __name__ == "__main__":
    unittest.main()
