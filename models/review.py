#!usr/bin/python3
'''This module defines a class Review'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Defines and object review  and inherits BaseModel class'''
    place_id = ""
    user_id = ""
    text = ""
