#!/usr/bin/python3
'''Defines a FileStorage Class for serialization and deserialisation'''
import json
from models.base_model import BaseModel
from models import base_model
from models.user import User
from models import user
from models import state
from models import city
from models import place
from models import amenity
from models import review


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

        class_atr = {
                user.User: ["email", "password", "first_name", "last_name"],
                state.State: ["name"],
                city.City: ["state_id", "name"],
                amenity.Amenity: ["name"],
                place.Place: ["city_id", "user_id", "name", "description",
                              "number_rooms", "number_bathrooms", "max_guest",
                              "price_by_night", "latitude", "longitude",
                              "amenity_ids"],
                review.Review: ["place_id", "user_id", "text"]
                }
        a_list = []

        # setting the id attributes
        for k, v in FileStorage.__objects.items():
            if isinstance(v, state.State):
                for obj in FileStorage.__objects.values():
                    if isinstance(obj, city.City):
                        setattr(obj, 'state_id', v.id)
            if isinstance(v, city.City):
                for obj in FileStorage.__objects.values():
                    if isinstance(obj, place.Place):
                        setattr(obj, 'city_id', v.id)
            if isinstance(v, user.User):
                for obj in FileStorage.__objects.values():
                    if isinstance(obj, place.Place):
                        setattr(obj, 'user_id', v.id)
            if isinstance(v, amenity.Amenity):
                a_list.append(v.id)
                for obj in FileStorage.__objects.values():
                    if isinstance(obj, place.Place):
                        setattr(obj, 'amenity_ids', a_list)
            if isinstance(v, place.Place):
                for obj in FileStorage.__objects.values():
                    if isinstance(obj, review.Review):
                        setattr(obj, 'place_id', v.id)
            if isinstance(v, user.User):
                for obj in FileStorage.__objects.values():
                    if isinstance(obj, review.Review):
                        setattr(obj, 'user_id', v.id)
        # plus adding class attribute
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
            if type(obj) in class_atr:
                for attr in class_atr[type(obj)]:
                    if hasattr(obj, attr):
                        data[attr] = getattr(obj, attr)

        with open(FileStorage.__file_path, "w", encoding='utf-8') as myf:
            k = json.dump(data, myf)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        # read the json file
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as myf:
                class_dic = json.load(myf)
        # convertt to class object
            module_list = [base_model, user, state, city, amenity, place,
                           review]

            for key, value in class_dic.items():
                name = key.split(".")
                class_n = name[0]

                for module in module_list:
                    class_name = getattr(module, class_n, None)
                    if class_name:
                        obj = class_name(**value)
                        self.new(obj)
                        break

        except FileNotFoundError:
            pass
