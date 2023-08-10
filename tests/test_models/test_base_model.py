#!/usr/bin/python3
'''Testing base classs in th module base'''
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Perform unittest for BaseModel class'''
    def test__class(self):
        '''test the existance of the class'''
        self.assertTrue(issubclass(BaseModel, object))
        self.assertFalse(issubclass(BaseModel, int))

    def test_id(self):
        '''test the object of id attribute'''
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(len(obj.id) == 36)
        self.assertFalse(obj.id == obj1.id)

    def test_created_at(self):
        '''test the attribute created_at'''
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(datetime.datetime.now(), obj.created_at)
        self.assertFalse(isinstance(obj.created_at, int))

    def test_update_at(self):
        '''test the attribute updated_at'''
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertTrue(datetime.datetime.now(), obj.updated_at)
        self.assertFalse(isinstance(obj.updated_at, int))

    def test_str(self):
        '''test the __str__ method'''
        obj = BaseModel()
        string = f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}'
        self.assertTrue(obj.id in str(obj))
        self.assertTrue('created_at' in obj.__str__())
        self.assertTrue('updated_at' in obj.__str__())
        self.assertTrue(obj.__class__.__name__ in str(obj))
        self.assertEqual(str(obj), string)
        with self.assertRaises(TypeError):
            obj.__str__(123)
        with self.assertRaises(TypeError):
            obj.__str__(["b", 'cv'])
    def test_save(self):
        '''test the save methode '''
        obj = BaseModel()
        obj.save()
        self.assertTrue(datetime.datetime.now(), obj.updated_at)
        with self.assertRaises(TypeError):
            obj.save(232)
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_to_dict(self):
        '''test the to_dict method'''
        obj = BaseModel()
        self.assertTrue(isinstance(obj.to_dict(), dict))
        # checking the keys 
        self.assertTrue("__class__" in obj.to_dict())
        self.assertTrue("id" in obj.to_dict())
        self.assertTrue("created_at" in obj.to_dict())
        self.assertTrue("updated_at" in obj.to_dict())
        
        # checking for type of attr
        self.assertTrue(isinstance(obj.to_dict()["created_at"], str))
        self.assertTrue(isinstance(obj.to_dict()["updated_at"], str))
        self.assertTrue(isinstance(obj.to_dict()["id"], str))
        self.assertTrue(isinstance(obj.to_dict()["__class__"], str))
        
        # isoformat testing
        iso_create = obj.created_at.isoformat()
        iso_update = obj.updated_at.isoformat()

        self.assertEqual(iso_create, obj.to_dict()["created_at"])
        self.assertTrue("T" in obj.to_dict()["created_at"])
        self.assertEqual(iso_update, obj.to_dict()["updated_at"])
        self.assertTrue("T" in obj.to_dict()["updated_at"])

        with self.assertRaises(TypeError):
            obj.to_dict(232)
        with self.assertRaises(TypeError):
            obj.to_dict([1, 3, 3])

    def test_module(self):
        '''test module withe arguments'''
        # pass an argument, test is id, created_at and updated
        obj = BaseModel(23)
        self.assertNotEqual(obj.id, 23)
        self.assertNotEqual(obj.created_at, 23)
        self.assertNotEqual(obj.updated_at, 23)

        # pass a string
        obj = BaseModel("bion")
        self.assertNotEqual(obj.id, "bion")
        self.assertNotEqual(obj.created_at, "bion")
        self.assertNotEqual(obj.updated_at, "bion")

    def test_module_args(self):
        '''passing more than one argument'''
        # pass a more thano one args
        obj = BaseModel("bion", 23)
        self.assertNotEqual(obj.id, "bion")
        self.assertNotEqual(obj.id, 23)
        self.assertNotEqual(obj.created_at, "bion")
        self.assertNotEqual(obj.created_at, 23)
        self.assertNotEqual(obj.updated_at, "bion")
        self.assertNotEqual(obj.updated_at, 23)


    def test_module_args(self):
        '''passing more than a list as argument'''
        # pass a more thano one args
        obj = BaseModel(["bion", 23])
        self.assertNotEqual(obj.id, "bion")
        self.assertNotEqual(obj.id, 23)
        self.assertNotEqual(obj.created_at, "bion")
        self.assertNotEqual(obj.created_at, 23)
        self.assertNotEqual(obj.updated_at, "bion")
        self.assertNotEqual(obj.updated_at, 23)

    def test_module_dict(self):
        '''passing a dictionary as arguments'''
        #  pass a dictionary
        args = {'my_number': 89, 'name': 'My First Model', 
                '__class__': 'BaseModel',
                'updated_at': '2017-09-28T21:05:54.119572',
                'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 
                'created_at': '2017-09-28T21:05:54.119427'
                }
        obj = BaseModel(**args)
        self.assertEqual(obj.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(obj.created_at, datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))
        self.assertEqual(obj.updated_at, datetime.datetime(2017, 9, 28, 21, 5, 54, 119572))
        self.assertEqual(obj.my_number, 89)
        self.assertEqual(obj.name, 'My First Model')
        self.assertNotEqual(obj.__class__, 'BaseModed')

        # pass an empty dict
    def test_empty_dict(self):
        '''passing an empty dictionary as arguments'''
        args = {}
        obj = BaseModel(**args)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))


    def test_mixed_args(self):
        '''passing a mixture of args and kwargs'''
        kwargs = {'my_number': 89, 'name': 'My First Model',
                '__class__': 'BaseModel',
                'updated_at': '2017-09-28T21:05:54.119572',
                'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                'created_at': '2017-09-28T21:05:54.119427'
                }
        arg = (1, 3, 5)
        obj = BaseModel(*arg, **kwargs)
        self.assertEqual(obj.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(obj.created_at, datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))
        self.assertEqual(obj.updated_at, datetime.datetime(2017, 9, 28, 21, 5, 54, 119572))
        self.assertEqual(obj.my_number, 89)
        self.assertEqual(obj.name, 'My First Model')
        self.assertNotEqual(obj.__class__, 'BaseModed')

    def test_one(self):
        '''passing just one arg in the dictionary'''
        kwargs = {'my_number': 89}
        obj = BaseModel(**kwargs)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(obj.my_number, 89)

    def test_two(self):
        '''test with more two args'''
        kwargs = {'my_number': 89, 'name': 'My First Model'}
        obj = BaseModel(**kwargs)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(obj.my_number, 89)
        self.assertEqual(obj.name, 'My First Model')

    def test_update_atr(self):
        '''update attributes only'''
        kwargs = {
                'updated_at': '2017-09-28T21:05:54.119572',
                'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                'created_at': '2017-09-28T21:05:54.119427'
                }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(obj.created_at, datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))
        self.assertEqual(obj.updated_at, datetime.datetime(2017, 9, 28, 21, 5, 54, 119572))

    def test_id_kwarg(self):
        '''test id attribute with passed as a int, string or iterable'''
        kwargs = {
                'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579'
                }

        obj = BaseModel(**kwargs)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertEqual(obj.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        # passing id as a int
        kwargs = {
                'id': 1234}

        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, 1234)
        # passing id as a string
        kwargs = {'id': 'comeagain'}

        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, 'comeagain')
        # passsing id a tuple
        kwargs = {'id': (1, 2, 3, 4)}

        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, (1, 2, 3, 4))

        # passing id an empty
        kwargs = {'id': None}

        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, None)

        kwargs = {'id': ''}
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, '')

    def test_create_kwarg(self):
        '''test created_at attribute with passed as a int, string or iterable'''
        kwargs = {'created_at': '2017-09-28T21:05:54.119427'}

        obj = BaseModel(**kwargs)
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertEqual(datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), obj.created_at)

    def test_create_int(self):
        ''' passing created_at as a int'''
        kwargs = {'created_at': 1234}
        
        with self.assertRaises(TypeError):
            obj = BaseModel(**kwargs)

    def test_create_str(self):
        ''' passing created as a string '''
        kwargs = {'created_at': "come"}

        with self.assertRaises(ValueError):
            obj = BaseModel(**kwargs)
        # passsing created_at as tuple
        kwargs = {'created_at': (1, 2)}

        with self.assertRaises(TypeError):
            obj = BaseModel(**kwargs)
    
    def test_create_None(self):
        ''' passing created as empty'''
        kwargs = {'created_at': None}
        with self.assertRaises(TypeError):
            obj = BaseModel(**kwargs)

        kwargs = {'created_at': ""}
        with self.assertRaises(ValueError):
            obj = BaseModel(**kwargs)

    def test_update_kwarg(self):
        '''test updated_at attribute with passed as a int, string or iterable'''
        kwargs = {'updated_at': '2017-09-28T21:05:54.119427'}

        obj = BaseModel(**kwargs)
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), obj.updated_at)

    def test_update_int(self):
        ''' passing updated_at as a int'''
        kwargs = {'updated_at': 1234}

        with self.assertRaises(TypeError):
            obj = BaseModel(**kwargs)

    def test_update_str(self):
        ''' passing updated as a string '''
        kwargs = {'updated_at': "come"}

        with self.assertRaises(ValueError):
            obj = BaseModel(**kwargs)
        # passsing updated_at as tuple
        kwargs = {'updated_at': (1, 2)}

        with self.assertRaises(TypeError):
            obj = BaseModel(**kwargs)

    def test_update_None(self):
        ''' passing updated as empty'''
        kwargs = {'updated_at': None}
        with self.assertRaises(TypeError):
            obj = BaseModel(**kwargs)

        kwargs = {'updated_at': ""}
        with self.assertRaises(ValueError):
            obj = BaseModel(**kwargs)
