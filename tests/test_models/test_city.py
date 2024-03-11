#!/usr/bin/python3
"""makes the unittests for all models/city.py.

Unittest classes:
    TestCityinstantiation
    TestCitysave
    TestCitytodict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests testing for the City class."""

    def test_noargs(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(City().id))

    def test_createdat_is_public(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updatedat_is_public(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_id_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_uniqueids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_createdat(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_updatedat(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

def test_str_representation(self):
    dt = datetime.today()
    dt_repr = repr(dt)
    cy = City()
    cy.id = "123456"
    cy.created_at = cy.updated_at = dt
    cystr = cy.__str__()

    expected_values = [
        "[City] (123456)",
        "'id': '123456'",
        "'created_at': " + dt_repr,
        "'updated_at': " + dt_repr
    ]

    for value in expected_values:
        self.assertIn(value, cystr)

    def test_args_unused(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_through_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_through_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests testing save method for City class."""

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
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_through_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

def test_save_updatesfile(self):
    cy = City()
    cy.save()
    cyid = "City." + cy.id
    found_cyid = False

    with open("file.json", "r") as f:
        for line in f:
            if cyid in line:
                found_cyid = True
                break

    self.assertTrue(found_cyid)


class TestCity_to_dict(unittest.TestCase):
    """Unittests testing  methods of the City class."""

    def test_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_correct_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

def test_to_dict_attributes(self):
    cy = City()
    cy.middle_name = "My_First_Model"
    cy.my_number = 89
    self.assertEqual("My_First_Model", cy.middle_name)

    dict_attributes = cy.to_dict()
    self.assertIn("my_number", dict_attributes)

def test_attributes_are_strs(self):
    cy = City()
    cy_dict = cy.to_dict()
    
    attributes = ["id", "created_at", "updated_at"]
    for attr in attributes:
        self.assertEqual(str, type(cy_dict[attr]))

def test_output(self):
    dt = datetime.today()
    cy = City()
    cy.id = "123456"
    cy.created_at = cy.updated_at = dt
    expected_dict = {
        'id': '123456',
        '__class__': 'City',
        'created_at': dt.isoformat(),
        'updated_at': dt.isoformat(),
    }
    assert cy.to_dict() == expected_dict

def test_dunder_dict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

def test_to_dict_through_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
