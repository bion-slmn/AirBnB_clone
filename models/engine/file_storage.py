#!/usr/bin/python3
'''Defines a FileStorage Class for serialization and deserialisation'''
import json
from models.base_model import BaseModel
from models import base_model


class FileStorage:
    '''This class defines method for serializes instances to a JSON
    file and deserializes JSON file to instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Return the private classs attribute object, which cotains
        ids of all instances stored'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = f'{obj.__class__.__name__}.{obj.id}'
        value = obj

        FileStorage.__objects[key] = value

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding='utf-8') as myf:
            k = json.dump(data, myf)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        # read the json file
        try:
            FileStorage.__objects.clear()

            with open(FileStorage.__file_path, "r", encoding='utf-8') as myf:
                class_dic = json.load(myf)
        # convertt to class object
            for key, value in class_dic.items():
                name = key.split(".")
                class_name = name[0]
                class_ = getattr(base_model, class_name)
                obj = class_(**value)
                self.new(obj)

        except FileNotFoundError:
            pass
