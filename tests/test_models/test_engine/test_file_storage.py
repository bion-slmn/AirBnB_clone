#!/usr/bin/python3
"""Defines unittest for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instance
    TestFileStorage_methods
"""
import os
import unittest
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                from models.base_model import BaseModel  # Update with the actual import path of BaseModel
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    cls = globals()[cls_name]
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance



if __name__ == "__main__":
    unittest.main()
