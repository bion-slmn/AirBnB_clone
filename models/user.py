#!/usr/bin/python3
'''This module defines the class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Defines a user and inherits the BaseModel class'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
