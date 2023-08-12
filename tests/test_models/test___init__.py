#!/usr/bin/python3
'''test the __init.py '''
import unittest
import models
from models.engine.file_storage import FileStorage


class Test__init(unittest.TestCase):
    '''test the file init of model'''
    def test_storage(self):
        ''' testing the storage variable'''
        self.assertTrue(isinstance(models.storage, FileStorage))
        self.assertTrue(hasattr(models, 'storage'))
