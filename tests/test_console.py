#!usr/bin/python3
'''This module tests the console created using cmd module'''
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd
import unittest
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    '''This tests the class class HBNBCommand(cmd.Cmd)'''
    def test_prompt(self):
        '''test the prompt in console'''
        self.assertTrue("(hbnb) ", HBNBCommand(cmd.Cmd).prompt)

    def test_quit(self):
        '''test the quit method'''
        txt = 'Quit command to exit the program'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(), txt)
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertTrue(HBNBCommand().onecmd("quit 22 33"))

    def test_EOF(self):
        '''test the EOF method'''
        txt = 'Exit the command interpeter by using ctr + D'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(), txt)
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertTrue(HBNBCommand().onecmd("EOF 22 33"))

    def test_empty_line(self):
        '''test the empty_line method'''
        txt = ''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue().strip(), txt)
