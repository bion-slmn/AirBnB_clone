#!/usr/bin/python3
''' Thi mododule performs unittests for city class'''
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''This class tests city class usnig unnittest'''
    def test_inhert(self):
        ''' test the  inheritance of th class'''
        obj = City()
        self.assertTrue(isinstance(obj, object))
        self.assertTrue(isinstance(obj, BaseModel))
        self.assertFalse(isinstance(obj, int))

    def test_attr_name(self):
        '''test the attributes of the city class and public'''
        obj = City()
        self.assertTrue(hasattr(obj, 'name'))
        self.assertTrue(isinstance(obj.name, str))
        self.assertEqual(len(obj.name), 0)

    def test_attr_state_id(self):
        '''test the stateid attribute of the city class and public'''
        obj = City()
        self.assertTrue(hasattr(obj, 'state_id'))
        self.assertTrue(isinstance(obj.state_id, str))
        self.assertEqual(len(obj.state_id), 0)

    def test_class_attr_name(self):
        ''' test that nmae is a class attribute'''
        obj = City()
        self.assertFalse("name" in obj.__dict__)
        self.assertTrue("name" in dir(obj))
        obj.name = 234
        self.assertTrue(obj.name == 234)

    def test_class_attr_state_id(self):
        ''' test that state_id is a class attribute'''
        obj = City()
        self.assertFalse("state_id" in obj.__dict__)
        self.assertTrue("state_id" in dir(obj))
        obj.state_id = "come"
        self.assertTrue(obj.state_id == "come")

    def test_inherited_att(self):
        ''' test inherited attributes in City'''
        obj = City()
        self.assertTrue('id' in obj.__dict__)
        self.assertIn('created_at', obj.__dict__)
        self.assertIn('updated_at', obj.__dict__)

    def test_inherited_method(self):
        '''test inherited methoods'''
        obj = City()
        self.assertIn('save', dir(obj))
        self.assertIn('to_dict', dir(obj))
        self.assertIn('__str__', dir(obj))

    def test_args_int(self):
        ''' test the city class with arguments passed'''
        # test with and int
        obj = City(123)
        self.assertNotEqual(obj.id, 123)
        self.assertNotEqual(obj.name, 123)
        self.assertNotEqual(obj.state_id, 123)
        self.assertNotEqual(obj.created_at, 123)
        self.assertNotEqual(obj.updated_at, 123)

    def test_args_string(self):
        ''' test the city class with string  arguments passed'''
        # test with and string
        obj = City('come')
        self.assertNotEqual(obj.id, 'come')
        self.assertNotEqual(obj.name, 'come')
        self.assertNotEqual(obj.state_id, 'come')
        self.assertNotEqual(obj.created_at, 'come')
        self.assertNotEqual(obj.updated_at, 'come')

    def test_args_many(self):
        ''' test the city class with many arguments passed'''
        # test with and more than one argument
        obj = City(1, 2)
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.name, 1)
        self.assertNotEqual(obj.name, 2)
        self.assertNotEqual(obj.state_id, 1)
        self.assertNotEqual(obj.state_id, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)

    def test_arg_tuples(self):
        ''' test the city class with a tuplea as arguments passed'''
        # test with a tuple or iterable
        obj = City((1, 2))
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.name, 1)
        self.assertNotEqual(obj.name, 2)
        self.assertNotEqual(obj.state_id, 1)
        self.assertNotEqual(obj.state_id, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)

    def test_args_NOne(self):
        ''' test the city class with None as  arguments passed'''
        # test with None
        obj = City(None)
        self.assertNotEqual(obj.id, None)
        self.assertNotEqual(obj.name, None)
        self.assertNotEqual(obj.state_id, None)
        self.assertNotEqual(obj.created_at, None)
        self.assertNotEqual(obj.updated_at, None)
