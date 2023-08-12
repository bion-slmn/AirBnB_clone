#!/usr/bin/python3
''' Thi mododule performs unittests for state class'''
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    '''This class tests state class usnig unnittest'''
    def test_inhert(self):
        ''' test the  inheritance of th class'''
        obj = State()
        self.assertTrue(isinstance(obj, object))
        self.assertTrue(isinstance(obj, BaseModel))
        self.assertFalse(isinstance(obj, int))

    def test_attr(self):
        '''test the attributes of the state class and public'''
        obj = State()
        self.assertTrue(hasattr(obj, 'name'))
        self.assertTrue(isinstance(obj.name, str))
        self.assertEqual(len(obj.name), 0)

    def test_class_attr(self):
        ''' test that nmae is a class attribute'''
        obj = State()
        self.assertFalse("name" in obj.__dict__)
        self.assertTrue("name" in dir(obj))

    def test_inherited_att(self):
        ''' test inherited attributes in State'''
        obj = State()
        self.assertTrue('id' in obj.__dict__)
        self.assertIn('created_at', obj.__dict__)
        self.assertIn('updated_at', obj.__dict__)

    def test_inherited_method(self):
        '''test inherited methoods'''
        obj = State()
        self.assertIn('save', dir(obj))
        self.assertIn('to_dict', dir(obj))
        self.assertIn('__str__', dir(obj))

    def test_args_int(self):
        ''' test the state class with arguments passed'''
        # test with and int
        obj = State(123)
        self.assertNotEqual(obj.id, 123)
        self.assertNotEqual(obj.name, 123)
        self.assertNotEqual(obj.created_at, 123)
        self.assertNotEqual(obj.updated_at, 123)

    def test_args_string(self):
        ''' test the state class with string  arguments passed'''
        # test with and string
        obj = State('come')
        self.assertNotEqual(obj.id, 'come')
        self.assertNotEqual(obj.name, 'come')
        self.assertNotEqual(obj.created_at, 'come')
        self.assertNotEqual(obj.updated_at, 'come')

    def test_args_many(self):
        ''' test the state class with many arguments passed'''
        # test with and more than one argument
        obj = State(1, 2)
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.name, 1)
        self.assertNotEqual(obj.name, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)

    def test_arg_tuples(self):
        ''' test the state class with a tuplea as arguments passed'''
        # test with a tuple or iterable
        obj = State((1, 2))
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.name, 1)
        self.assertNotEqual(obj.name, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)

    def test_args_NOne(self):
        ''' test the state class with None as  arguments passed'''
        # test with None
        obj = State(None)
        self.assertNotEqual(obj.id, None)
        self.assertNotEqual(obj.name, None)
        self.assertNotEqual(obj.created_at, None)
        self.assertNotEqual(obj.updated_at, None)
