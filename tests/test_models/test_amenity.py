#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import inspect
import unittest
storage_t = getenv("HBNB_TYPE_STORAGE")

class test_Amenity(test_basemodel):
    """ hnbnb pro """

    def __init__(self, *args, **kwargs):
        """ the init"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ first test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """try the usr"""
    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_inherit_basemodel(unittest.TestCase):
    """is base model the parent?"""
    def test_instance(self):
        """base is inatance?"""
        user = Amenity()
        self.assertIsInstance(user, Amenity)
        self.assertTrue(issubclass(type(user), BaseModel))

class test_Amenity_BaseModel(unittest.TestCase):
    """Testing user class"""
    def test_instances(self):
        with patch('models.amenity'):
            instance = Amenity()
            self.assertEqual(type(instance), Amenity)
            instance.name = "Barbie"
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], 'Barbie')
            self.assertEqual(inst_dict['__class__'], 'Amenity')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "Barbie")

    def test_user_id_and_createat(self):
        """testing id for every user"""
        user_1 = Amenity()
        sleep(2)
        user_2 = Amenity()
        sleep(2)
        user_3 = Amenity()
        sleep(2)

        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertTrue(user_1.created_at <= user_2.created_at)

class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's as an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_t == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")


    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        daaaaa = Amenity()
        sasfdaa =daaaaaa.to_dict()
        self.assertEqual(type(sasfdaa["updated_at"]), str)
        self.assertEqual(sasfdaa["created_at"],daaaaaa.created_at.strftime(t_format))
        self.assertEqual(type(sasfdaa["created_at"]), str)
        self.assertEqual(sasfdaa["updated_at"],daaaaaa.updated_at.strftime(t_format))
        self.assertEqual(sasfdaa["__class__"], "Amenity")

    def test_str(self):
        """test that the str method has the correct output"""
        nss = Amenity()
        string = "[Amenity] ({}) {}".format(nss.id, nss.__dict__)
        self.assertEqual(string, str(nss))

if __name__ == "__main__":
    unittest.main()