#!/usr/bin/python3
''' Thi mododule performs unittests for place class'''
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    '''This class tests place class usnig unnittest'''
    def test_inhert(self):
        ''' test the  inheritance of th class'''
        obj = Place()
        self.assertTrue(isinstance(obj, object))
        self.assertTrue(isinstance(obj, BaseModel))
        self.assertFalse(isinstance(obj, int))

    def test_attr_name(self):
        '''test the name attributes of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'name'))
        self.assertTrue(isinstance(obj.name, str))
        self.assertEqual(len(obj.name), 0)

    def test_class_attr_name(self):
        ''' test that name is a class attribute'''
        obj = Place()
        self.assertFalse("name" in obj.__dict__)
        self.assertTrue("name" in dir(obj))
        obj.name = "some"
        self.assertEqual(obj.name, "some")
        self.assertNotEqual(len(obj.name), 0)

    def test_attr_city_id(self):
        '''test the city_id of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'city_id'))
        self.assertTrue(isinstance(obj.city_id, str))
        self.assertEqual(len(obj.city_id), 0)

    def test_class_attr_city_id(self):
        ''' test that city_id is a class attribute'''
        obj = Place()
        self.assertFalse("city_id" in obj.__dict__)
        self.assertTrue("city_id" in dir(obj))
        obj.city_id = "some"
        self.assertEqual(obj.city_id, "some")
        self.assertNotEqual(len(obj.city_id), 0)

    def test_attr_user_id(self):
        '''test the user_id of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(isinstance(obj.user_id, str))
        self.assertEqual(len(obj.user_id), 0)

    def test_class_attr_user_id(self):
        ''' test that user_id is a class attribute'''
        obj = Place()
        self.assertFalse("user_id" in obj.__dict__)
        self.assertTrue("user_id" in dir(obj))
        obj.user_id = "some"
        self.assertEqual(obj.user_id, "some")
        self.assertNotEqual(len(obj.user_id), 0)

    def test_attr_description(self):
        '''test the description of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'description'))
        self.assertTrue(isinstance(obj.description, str))
        self.assertEqual(len(obj.description), 0)

    def test_class_attr_description(self):
        ''' test that description is a class attribute'''
        obj = Place()
        self.assertFalse("description" in obj.__dict__)
        self.assertTrue("description" in dir(obj))
        obj.description = "some"
        self.assertEqual(obj.description, "some")
        self.assertNotEqual(len(obj.description), 0)

    def test_attr_number_rooms(self):
        '''test the number_rooms of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'number_rooms'))
        self.assertTrue(isinstance(obj.number_rooms, int))
        self.assertEqual(obj.number_rooms, 0)

    def test_class_attr_number_rooms(self):
        ''' test that number_rooms is a class attribute'''
        obj = Place()
        self.assertFalse("number_rooms" in obj.__dict__)
        self.assertTrue("number_rooms" in dir(obj))
        obj.number_rooms = 123
        self.assertEqual(obj.number_rooms, 123)

    def test_attr_number_bathrooms(self):
        '''test the number_bathrooms of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'number_bathrooms'))
        self.assertTrue(isinstance(obj.number_bathrooms, int))
        self.assertEqual(obj.number_bathrooms, 0)

    def test_class_attr_number_bathrooms(self):
        ''' test that number_bathrooms is a class attribute'''
        obj = Place()
        self.assertFalse("number_bathrooms" in obj.__dict__)
        self.assertTrue("number_bathrooms" in dir(obj))
        obj.number_bathrooms = 123
        self.assertEqual(obj.number_bathrooms, 123)

    def test_attr_max_guest(self):
        '''test the max_guest of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'max_guest'))
        self.assertTrue(isinstance(obj.max_guest, int))
        self.assertEqual(obj.max_guest, 0)

    def test_class_attr_max_guest(self):
        ''' test that max_guest is a class attribute'''
        obj = Place()
        self.assertFalse("max_guest" in obj.__dict__)
        self.assertTrue("max_guest" in dir(obj))
        obj.max_guest = 123
        self.assertEqual(obj.max_guest, 123)

    def test_attr_price_by_night(self):
        '''test the price_by_night of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'price_by_night'))
        self.assertTrue(isinstance(obj.price_by_night, int))
        self.assertEqual(obj.price_by_night, 0)

    def test_class_attr_price_by_night(self):
        ''' test that price_by_night is a class attribute'''
        obj = Place()
        self.assertFalse("price_by_night" in obj.__dict__)
        self.assertTrue("price_by_night" in dir(obj))
        obj.price_by_night = 123
        self.assertEqual(obj.price_by_night, 123)

    def test_attr_latitude(self):
        '''test the latitude of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'latitude'))
        self.assertTrue(isinstance(obj.latitude, float))
        self.assertEqual(obj.latitude, 0)

    def test_class_attr_latitude(self):
        ''' test that latitude is a class attribute'''
        obj = Place()
        self.assertFalse("latitude" in obj.__dict__)
        self.assertTrue("latitude" in dir(obj))
        obj.latitude = 123.0
        self.assertEqual(obj.latitude, 123.0)

    def test_attr_longitude(self):
        '''test the longitude of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'longitude'))
        self.assertTrue(isinstance(obj.longitude, float))
        self.assertEqual(obj.longitude, 0)

    def test_class_attr_longitude(self):
        ''' test that longitude is a class attribute'''
        obj = Place()
        self.assertFalse("longitude" in obj.__dict__)
        self.assertTrue("longitude" in dir(obj))
        obj.longitude = 123.0
        self.assertEqual(obj.longitude, 123.0)

    def test_attr_amenity_ids(self):
        '''test the amenity_ids of the place class tthat its public'''
        obj = Place()
        self.assertTrue(hasattr(obj, 'amenity_ids'))
        self.assertTrue(isinstance(obj.amenity_ids, list))
        self.assertEqual(len(obj.amenity_ids), 0)

    def test_class_attr_amenity_ids(self):
        ''' test that amenity_ids is a class attribute'''
        obj = Place()
        self.assertFalse("amenity_ids" in obj.__dict__)
        self.assertTrue("amenity_ids" in dir(obj))
        obj.amenity_ids = [1, 2]
        self.assertEqual(obj.amenity_ids, [1, 2])

    def test_inherited_att(self):
        ''' test inherited attributes in Place'''
        obj = Place()
        self.assertTrue('id' in obj.__dict__)
        self.assertIn('created_at', obj.__dict__)
        self.assertIn('updated_at', obj.__dict__)

    def test_inherited_method(self):
        '''test inherited methoods'''
        obj = Place()
        self.assertIn('save', dir(obj))
        self.assertIn('to_dict', dir(obj))
        self.assertIn('__str__', dir(obj))

    def test_args_int(self):
        ''' test the place class with arguments passed'''
        # test with and int for inherited attribute
        obj = Place(123)
        self.assertNotEqual(obj.id, 123)
        self.assertNotEqual(obj.name, 123)
        self.assertNotEqual(obj.created_at, 123)
        self.assertNotEqual(obj.updated_at, 123)

    def test_int_class_att(self):
        ''' test class itributes when passed int'''
        obj = Place(1)
        self.assertNotEqual(obj.name, 1)
        self.assertNotEqual(obj.city_id, 1)
        self.assertNotEqual(obj.user_id, 1)
        self.assertNotEqual(obj.number_rooms, 1)
        self.assertNotEqual(obj.description, 1)
        self.assertNotEqual(obj.max_guest, 1)
        self.assertNotEqual(obj.number_bathrooms, 1)
        self.assertNotEqual(obj.price_by_night, 1)
        self.assertNotEqual(obj.latitude, 1)
        self.assertNotEqual(obj.longitude, 1)
        self.assertNotEqual(obj.amenity_ids, 1)

    def test_args_string(self):
        ''' test the place class with string for inherite arguments'''
        # test with and string
        obj = Place('come')
        self.assertNotEqual(obj.id, 'come')
        self.assertNotEqual(obj.created_at, 'come')
        self.assertNotEqual(obj.updated_at, 'come')

    def test_str_class_att(self):
        ''' test class itributes when passed string'''
        obj = Place('b')
        self.assertNotEqual(obj.name, 'b')
        self.assertNotEqual(obj.city_id, 'b')
        self.assertNotEqual(obj.user_id, 'b')
        self.assertNotEqual(obj.number_rooms, 'b')
        self.assertNotEqual(obj.description, 'b')
        self.assertNotEqual(obj.max_guest, 'b')
        self.assertNotEqual(obj.number_bathrooms, 'b')
        self.assertNotEqual(obj.price_by_night, 'b')
        self.assertNotEqual(obj.latitude, 'b')
        self.assertNotEqual(obj.longitude, 'b')
        self.assertNotEqual(obj.amenity_ids, 'b')

    def test_args_many(self):
        ''' test the inherited atts ofplace class with many
        arguments passed'''
        # test with and more than one argument
        obj = Place(1, 2)
        self.assertNotEqual(obj.id, 1)
        self.assertNotEqual(obj.id, 2)
        self.assertNotEqual(obj.created_at, 1)
        self.assertNotEqual(obj.created_at, 2)
        self.assertNotEqual(obj.updated_at, 1)
        self.assertNotEqual(obj.updated_at, 2)

    def test_many_class_att(self):
        ''' test class itributes when passed class many args'''
        obj = Place(1, 2)
        self.assertNotEqual(obj.name, 2)
        self.assertNotEqual(obj.city_id, 2)
        self.assertNotEqual(obj.user_id, 2)
        self.assertNotEqual(obj.number_rooms, 2)
        self.assertNotEqual(obj.description, 2)
        self.assertNotEqual(obj.max_guest, 2)
        self.assertNotEqual(obj.number_bathrooms, 2)
        self.assertNotEqual(obj.price_by_night, 2)
        self.assertNotEqual(obj.latitude, 2)
        self.assertNotEqual(obj.longitude, 2)
        self.assertNotEqual(obj.amenity_ids, 2)
        self.assertNotEqual(obj.name, 1)
        self.assertNotEqual(obj.city_id, 1)
        self.assertNotEqual(obj.user_id, 1)
        self.assertNotEqual(obj.number_rooms, 1)
        self.assertNotEqual(obj.description, 1)
        self.assertNotEqual(obj.max_guest, 1)
        self.assertNotEqual(obj.number_bathrooms, 1)
        self.assertNotEqual(obj.price_by_night, 1)
        self.assertNotEqual(obj.latitude, 1)
        self.assertNotEqual(obj.longitude, 1)
        self.assertNotEqual(obj.amenity_ids, 1)

    def test_arg_list(self):
        ''' test the inherited place class with a list
        as arguments passed'''
        # test with an iterable
        obj = Place([1, 2])
        self.assertNotEqual(obj.id, [1, 2])
        self.assertNotEqual(obj.created_at, [1, 2])
        self.assertNotEqual(obj.updated_at, [1, 2])

        # testing class att with list
        self.assertNotEqual(obj.name, [1, 2])
        self.assertNotEqual(obj.city_id, [1, 2])
        self.assertNotEqual(obj.user_id, [1, 2])
        self.assertNotEqual(obj.number_rooms, [1, 2])
        self.assertNotEqual(obj.description, [1, 2])
        self.assertNotEqual(obj.max_guest, [1, 2])
        self.assertNotEqual(obj.number_bathrooms, [1, 2])
        self.assertNotEqual(obj.price_by_night, [1, 2])
        self.assertNotEqual(obj.latitude, [1, 2])
        self.assertNotEqual(obj.longitude, [1, 2])
        self.assertNotEqual(obj.amenity_ids, [1, 2])

    def test_args_NOne(self):
        ''' test the place class with None as  arguments passed'''
        # test with None
        obj = Place(None)
        self.assertNotEqual(obj.id, None)
        self.assertNotEqual(obj.name, None)
        self.assertNotEqual(obj.created_at, None)
        self.assertNotEqual(obj.updated_at, None)
        self.assertNotEqual(obj.name, None)
        self.assertNotEqual(obj.city_id, None)
        self.assertNotEqual(obj.user_id, None)
        self.assertNotEqual(obj.number_rooms, None)
        self.assertNotEqual(obj.description, None)
        self.assertNotEqual(obj.max_guest, None)
        self.assertNotEqual(obj.number_bathrooms, None)
        self.assertNotEqual(obj.price_by_night, None)
        self.assertNotEqual(obj.latitude, None)
        self.assertNotEqual(obj.longitude, None)
        self.assertNotEqual(obj.amenity_ids, None)

    def test_with_float(self):
        '''test with float'''
        obj = Place(1.1)
        self.assertNotEqual(obj.id, 1.1)
        self.assertNotEqual(obj.name, 1.1)
        self.assertNotEqual(obj.created_at, 1.1)
        self.assertNotEqual(obj.updated_at, 1.1)
        self.assertNotEqual(obj.name, 1.1)
        self.assertNotEqual(obj.city_id, 1.1)
        self.assertNotEqual(obj.user_id, 1.1)
        self.assertNotEqual(obj.number_rooms, 1.1)
        self.assertNotEqual(obj.description, 1.1)
        self.assertNotEqual(obj.max_guest, 1.1)
        self.assertNotEqual(obj.number_bathrooms, 1.1)
        self.assertNotEqual(obj.price_by_night, 1.1)
        self.assertNotEqual(obj.latitude, 1.1)
        self.assertNotEqual(obj.longitude, 1.1)
        self.assertNotEqual(obj.amenity_ids, 1.1)
