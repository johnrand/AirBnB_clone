#!/usr/bin/python3
"""Unittest for console([..]) for task 17"""
import unittest
import json
import os
from shutil import copy2
import cmd

from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """example1: this will Tests console command interpreter.

    """
    __objects_backup = storage._FileStorage__objects
    json_file = storage._FileStorage__file_path
    json_file_backup = storage._FileStorage__file_path + '.bup'

    @classmethod
    def setUpClass(cls):
        """this is for the setup Setup for all tests in module.
        """
        storage._FileStorage__objects = dict()
        while os.path.exists(cls.json_file):
            copy2(cls.json_file, cls.json_file_backup)
            os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        """this  is for Teardown after all tests in module.
        """
        storage._FileStorage__objects = cls.__objects_backup
        while os.path.exists(cls.json_file_backup):
            copy2(cls.json_file_backup, cls.json_file)
            os.remove(cls.json_file_backup)

    def tearDown(self):
        """if Any cleanup, per test method.
        """
        try:
            del (s1, s2)
        except NameError:
            pass
        storage._FileStorage__objects = dict()
        while os.path.exists(type(self).json_file):
            os.remove(type(self).json_file)

    def test_Console(self):
        """example 2: this will Tests console command interpreter.
        """
        self.assertIsNotNone(HBNBCommand())
        def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("EOF  help  quit", output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # UUID length

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertIn("[User] ({})".format(obj_id), output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User {}".format(obj_id))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

