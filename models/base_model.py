#!/usr/bin/python3
'''This module defines a class BaseModel'''
import uuid
import datetime
import models


class BaseModel():
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''initialises public attributes for the class
        args: positional arguments wont be used
        kwargs: keyword args will be used
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            f_date = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.strptime(v, f_date)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        ''' Return a human readable format of the class'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' updates the attribute updated_at with the current datetime'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of the class
        including the class name for reconstruction'''

        # create a dictionary for class
        class_dic = {"__class__": self.__class__.__name__}
        obj_dic = self.__dict__.copy()
        # update the create_at and update_at to ISO and to string

        obj_dic["created_at"] = self.created_at.isoformat()
        obj_dic["updated_at"] = self.updated_at.isoformat()

        # include the class in the dict
        obj_dic.update(class_dic)

        return obj_dic
