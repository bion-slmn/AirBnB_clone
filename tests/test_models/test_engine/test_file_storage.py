#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    '''Unittesest for class Filestorage'''

    # test the class
    def test_class(self):
        '''test that it doesnt inherit any other thing'''
        ob = FileStorage()
        self.assertTrue(isinstance(ob, object))
        self.assertFalse(isinstance(ob, BaseModel))

    def test_class_attr(self):
        '''test file_path is a private class attribute'''
        ob = FileStorage()
        self.assertTrue(isinstance(ob._FileStorage__file_path, str))
        self.assertFalse(hasattr(ob, 'file_path'))
        self.assertNotIn('filepath', dir(ob))
        self.assertNotIn('filepath', ob.__dict__)

    def test_class_attr_file(self):
        '''test file_path is a private class attribute'''
        ob = FileStorage()
        self.assertTrue(isinstance(ob._FileStorage__file_path, str))
        self.assertFalse(hasattr(ob, 'file_path'))
        self.assertNotIn('filepath', dir(ob))
        self.assertNotIn('filepath', ob.__dict__)
        self.assertTrue(ob._FileStorage__file_path, 'file.json')

    def test_class_attr_object(self):
        '''test object is a private class attribute'''
        ob = FileStorage()
        self.assertTrue(isinstance(ob._FileStorage__objects, dict))
        self.assertFalse(hasattr(ob, 'objects'))
        self.assertNotIn('objects', dir(ob))
        self.assertNotIn('objects', ob.__dict__)
        self.assertTrue(ob._FileStorage__objects, {})

    def test_all_method(self):
        ''' test that its a public method an returns a dictonary'''
        self.assertEqual(dict, type(models.storage.all()))
        self.assertIn('all', dir(models.storage))

    def test_new_method(self):
        ''' test that its a public method and it sets the object '''
        self.assertIn('new', dir(models.storage))
        bm = BaseModel()
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        with self.assertRaises(AttributeError):
            models.storage.new(21)

        self.assertTrue(models.storage._FileStorage__objects != {})

        us = User()
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertTrue(models.storage._FileStorage__objects != {})

        st = State()
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertTrue(models.storage._FileStorage__objects != {})

        pl = Place()
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertTrue(models.storage._FileStorage__objects != {})

        ct = City()
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())
        self.assertTrue(models.storage._FileStorage__objects != {})

        am = Amenity()
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertTrue(models.storage._FileStorage__objects != {})

        rw = Review()
        self.assertIn("Review." + rw.id, models.storage.all().keys())
        self.assertIn(rw, models.storage.all().values())
        self.assertTrue(models.storage._FileStorage__objects != {})

        with self.assertRaises(TypeError):
            models.storage.new(us, 1)

    def test_save(self):
        '''test the save method '''
        b = BaseModel()
        models.storage.new(b)
        u = User()
        models.storage.new(u)
        s = State()
        models.storage.new(s)
        p = Place()
        models.storage.new(p)
        c = City()
        models.storage.new(c)
        a = Amenity()
        models.storage.new(a)
        rv = Review()
        models.storage.new(rv)
        models.storage.save()

        self.assertTrue(os.stat('file.json').st_size != 0)
        with open('file.json', encoding='utf-8') as f:
            r = f.read()
            self.assertTrue(isinstance(r, str))
            self.assertIn("BaseModel." + b.id, r)
            self.assertIn("User." + u.id, r)
            self.assertIn("State." + s.id, r)
            self.assertIn("Place." + p.id, r)
            self.assertIn("City." + c.id, r)
            self.assertIn("Amenity." + a.id, r)
            self.assertIn("Review." + rv.id, r)

        with self.assertRaises(TypeError):
            models.storage.save(u, 1)

        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        '''test reload method for all the classes'''
        b = BaseModel()
        models.storage.new(b)
        u = User()
        models.storage.new(u)
        s = State()
        models.storage.new(s)
        p = Place()
        models.storage.new(p)
        c = City()
        models.storage.new(c)
        a = Amenity()
        models.storage.new(a)
        rv = Review()
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        dic = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b.id, dic)
        self.assertIn("User." + u.id, dic)
        self.assertIn("State." + s.id, dic)
        self.assertIn("Place." + p.id, dic)
        self.assertIn("City." + c.id, dic)
        self.assertIn("Amenity." + a.id, dic)
        self.assertIn("Review." + rv.id, dic)

    def test_reload_args(self):
        '''test reload with arguments passed'''
        with self.assertRaises(TypeError):
            models.storage.reload('u')

        with self.assertRaises(TypeError):
            models.storage.reload(None)

        with self.assertRaises(TypeError):
            models.storage.save(1, 1)

        with self.assertRaises(TypeError):
            models.storage.save([1, 2])
