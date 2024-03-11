#!/usr/bin/python3
"""makes unittests for all models/state.py.

Unittest classes:
    TestStateinstantiation
    TestStatesave
    TestStatetodict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateinstantiation(unittest.TestCase):
    """Unittests testing of the State class."""

    def test_noargs(self):
        self.assertEqual(State, type(State()))

    def test_name_attribute(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_two_states_uniqueids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_states_createdat(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_two_states_updatedat(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        ststr = st.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_new_instance_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_args_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instantiation_through_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "345")
        self.assertEqual(st.created_at, dt)
        self.assertEqual(st.updated_at, dt)

    def test_instantiation_through_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateToDict(unittest.TestCase):
    """Unittests testing methods of the State class."""

    def test_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_correct_keys(self):
        st = State()
        expected_keys = ["id", "created_at", "updated_at", "__class__"]
        dict_keys = st.to_dict().keys()

        i = 0
        while i < len(expected_keys):
            self.assertIn(expected_keys[i], dict_keys)
            i += 1

    def test_to_added_attributes(self):
        st = State()
        st.middle_name = "My_First_Model"
        st.my_number = 89
        self.assertEqual("My_First_Model", st.middle_name)

        dict_keys = st.to_dict().keys()
        self.assertIn("my_number", dict_keys)

    def test_to_attributes_are_strs(self):
        st = State()
        st_dict = st.to_dict()

        expected_keys = ["id", "created_at", "updated_at"]
        i = 0
        while i < len(expected_keys):
            self.assertEqual(str, type(st_dict[expected_keys[i]]))
            i += 1

    def test_output(self):
        dt = datetime.today()
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), expected_dict)

    def test_dunder_dict(self):
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

    def test_to_dict_through_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)


class TestStatesave(unittest.TestCase):
    """Unittests testing save methods for State class."""

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
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    def test_twosaves(self):
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        second_updated_at = st.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_updated_at, st.updated_at)

    def test_save_through_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updatesfile(self):
        st = State()
        st.save()
        stid = "State." + st.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


if __name__ == "__main__":
    unittest.main()
