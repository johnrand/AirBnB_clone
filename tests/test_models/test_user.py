#!/usr/bin/python3
"""makes unittests for all models/user.py.

Unittest classes:
    TestUserinstantiation
    TestUsersave
    TestUsertodict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests testing the User class."""

    def test_noargs(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_uniqueids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_createdat(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_updatedat(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_correct_keys(self):
        us = User()
        user_dict = us.to_dict()
        keys_to_check = ["id", "created_at", "updated_at", "__class__"]
        i = 0
        while i < len(keys_to_check):
            self.assertIn(keys_to_check[i], user_dict)
            i += 1

    def test_to_added_attributes(self):
        us = User()
        us.middle_name = "My_First_Model"
        us.my_number = 89
        self.assertEqual("My_First_Model", us.middle_name)
        user_dict = us.to_dict()
        self.assertIn("my_number", user_dict)

    def test_to_attributes_are_strs(self):
        us = User()
        us_dict = us.to_dict()
        keys_to_check = ["id", "created_at", "updated_at"]
        i = 0
        while i < len(keys_to_check):
            self.assertEqual(str, type(us_dict[keys_to_check[i]]))
            i += 1

    def test_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), expected_dict)

    def test_dunder_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_through_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


class TestUsersave(unittest.TestCase):
    """Unittests testing save method  the  class."""

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

    def test_onesave(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_twosaves(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_through_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updatesfile(self):
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


if __name__ == "__main__":
    unittest.main()
