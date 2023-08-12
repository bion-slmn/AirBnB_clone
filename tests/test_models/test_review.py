#!/usr/bin/python3
''' Thi mododule performs unittests for review class'''
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    '''This class tests review class usnig unnittest'''
    def test_inhert(self):
        ''' test the  inheritance of th class'''
        obj = Review()
        self.assertTrue(isinstance(obj, object))
        self.assertTrue(isinstance(obj, BaseModel))
        self.assertFalse(isinstance(obj, int))

    def test_attr_text(self):
        '''test the attribute text of the review class is public'''
        obj = Review()
        self.assertTrue(hasattr(obj, 'text'))
        self.assertTrue(isinstance(obj.text, str))
        self.assertEqual(len(obj.text), 0)

    def test_class_attr_text(self):
        ''' test that text is a class attribute'''
        obj = Review()
        self.assertFalse("text" in obj.__dict__)
        self.assertTrue("text" in dir(obj))

    def test_attr_user_id(self):
        '''test the attribute user_id of the review class is public'''
        obj = Review()
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(isinstance(obj.user_id, str))
        self.assertEqual(len(obj.user_id), 0)

    def test_class_attr_user_id(self):
        ''' test that user_id is a class attribute'''
        obj = Review()
        self.assertFalse("user_id" in obj.__dict__)
        self.assertTrue("user_id" in dir(obj))

    def test_attr_place_id(self):
        '''test the attribute place_id of the review class is public'''
        obj = Review()
        self.assertTrue(hasattr(obj, 'place_id'))
        self.assertTrue(isinstance(obj.place_id, str))
        self.assertEqual(len(obj.place_id), 0)

    def test_class_attr_place_id(self):
        ''' test that place_id is a class attribute'''
        obj = Review()
        self.assertFalse("place_id" in obj.__dict__)
        self.assertTrue("place_id" in dir(obj))

    def test_inherited_att(self):
        ''' test inherited attributes in Review'''
        obj = Review()
        self.assertTrue('id' in obj.__dict__)
        self.assertIn('created_at', obj.__dict__)
        self.assertIn('updated_at', obj.__dict__)

    def test_inherited_method(self):
        '''test inherited methoods'''
        obj = Review()
        self.assertIn('save', dir(obj))
        self.assertIn('to_dict', dir(obj))
        self.assertIn('__str__', dir(obj))

    def test_args_int(self):
        ''' test the review class with arguments passed'''
        # test with and int
        obj = Review(123)
        self.assertNotEqual(obj.id, 123)
        self.assertNotEqual(obj.text, 123)
        self.assertNotEqual(obj.created_at, 123)
        self.assertNotEqual(obj.updated_at, 123)
        self.assertNotEqual(obj.user_id, 123)
        self.assertNotEqual(obj.place_id, 123)

    def test_args_string(self):
        ''' test the review class with string  arguments passed'''
        # test with and string
        obj = Review('come')
        self.assertNotEqual(obj.id, 'come')
        self.assertNotEqual(obj.text, 'come')
        self.assertNotEqual(obj.created_at, 'come')
        self.assertNotEqual(obj.updated_at, 'come')
        self.assertNotEqual(obj.user_id, 'come')
        self.assertNotEqual(obj.place_id, 'come')

    def test_args_many(self):
        ''' test the review class with many arguments passed'''
        # test with and more than one argument
        obj = Review(1, 2)
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.text, 1)
        self.assertNotEqual(obj.text, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)
        self.assertNotEqual(obj.user_id, 2)
        self.assertNotEqual(obj.place_id, 2)
        self.assertNotEqual(obj.user_id, 1)
        self.assertNotEqual(obj.place_id, 1)

    def test_arg_tuples(self):
        ''' test the review class with a tuplea as arguments passed'''
        # test with a tuple or iterable
        obj = Review((1, 2))
        self.assertNotEqual(obj.id, (1, 2))
        self.assertNotEqual(obj.text, (1, 2))
        self.assertNotEqual(obj.created_at, (1, 2))
        self.assertNotEqual(obj.updated_at, (1, 2))
        self.assertNotEqual(obj.user_id, (1, 2))
        self.assertNotEqual(obj.place_id, (1, 2))

    def test_args_NOne(self):
        ''' test the review class with None as  arguments passed'''
        # test with None
        obj = Review(None)
        self.assertNotEqual(obj.id, None)
        self.assertNotEqual(obj.text, None)
        self.assertNotEqual(obj.created_at, None)
        self.assertNotEqual(obj.updated_at, None)
        self.assertNotEqual(obj.user_id, None)
        self.assertNotEqual(obj.place_id, None)
