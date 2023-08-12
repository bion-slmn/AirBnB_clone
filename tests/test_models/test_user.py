#!/usr/bin/python3
''' Thi mododule performs unittests for user class'''
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''This class tests user class usnig unnittest'''
    def test_inhert(self):
        ''' test the  inheritance of th class'''
        obj = User()
        self.assertTrue(isinstance(obj, object))
        self.assertTrue(isinstance(obj, BaseModel))
        self.assertFalse(isinstance(obj, int))

    def test_attr_email(self):
        '''test the attribute email of the user class is public'''
        obj = User()
        self.assertTrue(hasattr(obj, 'email'))
        self.assertTrue(isinstance(obj.email, str))
        self.assertEqual(len(obj.email), 0)

    def test_class_attr_email(self):
        ''' test that email is a class attribute'''
        obj = User()
        self.assertFalse("email" in obj.__dict__)
        self.assertTrue("email" in dir(obj))

    def test_attr_password(self):
        '''test the attribute password of the user class is public'''
        obj = User()
        self.assertTrue(hasattr(obj, 'password'))
        self.assertTrue(isinstance(obj.password, str))
        self.assertEqual(len(obj.password), 0)

    def test_class_attr_password(self):
        ''' test that password is a class attribute'''
        obj = User()
        self.assertFalse("password" in obj.__dict__)
        self.assertTrue("password" in dir(obj))

    def test_attr_first_name(self):
        '''test the attribute first_name of the user class is public'''
        obj = User()
        self.assertTrue(hasattr(obj, 'first_name'))
        self.assertTrue(isinstance(obj.first_name, str))
        self.assertEqual(len(obj.first_name), 0)

    def test_class_attr_first_name(self):
        ''' test that first_name is a class attribute'''
        obj = User()
        self.assertFalse("first_name" in obj.__dict__)
        self.assertTrue("first_name" in dir(obj))

    def test_attr_last_name(self):
        '''test the attribute first_name of the user class is public'''
        obj = User()
        self.assertTrue(hasattr(obj, 'last_name'))
        self.assertTrue(isinstance(obj.last_name, str))
        self.assertEqual(len(obj.last_name), 0)

    def test_class_attr_last_name(self):
        ''' test that last_name is a class attribute'''
        obj = User()
        self.assertFalse("last_name" in obj.__dict__)
        self.assertTrue("last_name" in dir(obj))

    def test_inherited_att(self):
        ''' test inherited attributes in User'''
        obj = User()
        self.assertTrue('id' in obj.__dict__)
        self.assertIn('created_at', obj.__dict__)
        self.assertIn('updated_at', obj.__dict__)

    def test_inherited_method(self):
        '''test inherited methoods'''
        obj = User()
        self.assertIn('save', dir(obj))
        self.assertIn('to_dict', dir(obj))
        self.assertIn('__str__', dir(obj))

    def test_args_int(self):
        ''' test the user class with arguments passed'''
        # test with and int
        obj = User(123)
        self.assertNotEqual(obj.id, 123)
        self.assertNotEqual(obj.email, 123)
        self.assertNotEqual(obj.created_at, 123)
        self.assertNotEqual(obj.updated_at, 123)
        self.assertNotEqual(obj.password, 123)
        self.assertNotEqual(obj.first_name, 123)
        self.assertNotEqual(obj.last_name, 123)

    def test_args_string(self):
        ''' test the user class with string  arguments passed'''
        # test with and string
        obj = User('come')
        self.assertNotEqual(obj.id, 'come')
        self.assertNotEqual(obj.email, 'come')
        self.assertNotEqual(obj.created_at, 'come')
        self.assertNotEqual(obj.updated_at, 'come')
        self.assertNotEqual(obj.password, 'come')
        self.assertNotEqual(obj.first_name, 'come')
        self.assertNotEqual(obj.last_name, 'come')

    def test_args_many(self):
        ''' test the user class with many arguments passed'''
        # test with and more than one argument
        obj = User(1, 2)
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.email, 1)
        self.assertNotEqual(obj.email, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)
        self.assertNotEqual(obj.password, 2)
        self.assertNotEqual(obj.first_name, 2)
        self.assertNotEqual(obj.password, 1)
        self.assertNotEqual(obj.first_name, 1)
        self.assertNotEqual(obj.last_name, 1)
        self.assertNotEqual(obj.last_name, 2)

    def test_arg_tuples(self):
        ''' test the user class with a tuplea as arguments passed'''
        # test with a tuple or iterable
        obj = User((1, 2))
        self.assertNotEqual(obj.id, (1, 2))
        self.assertNotEqual(obj.email, (1, 2))
        self.assertNotEqual(obj.created_at, (1, 2))
        self.assertNotEqual(obj.updated_at, (1, 2))
        self.assertNotEqual(obj.password, (1, 2))
        self.assertNotEqual(obj.first_name, (1, 2))
        self.assertNotEqual(obj.last_name, (1, 2))

    def test_args_NOne(self):
        ''' test the user class with None as  arguments passed'''
        # test with None
        obj = User(None)
        self.assertNotEqual(obj.id, None)
        self.assertNotEqual(obj.email, None)
        self.assertNotEqual(obj.created_at, None)
        self.assertNotEqual(obj.updated_at, None)
        self.assertNotEqual(obj.password, None)
        self.assertNotEqual(obj.first_name, None)
        self.assertNotEqual(obj.last_name, None)
