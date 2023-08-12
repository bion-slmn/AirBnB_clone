#!usr/bin/python3
''' This module defines City class'''
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    '''Defines a city and inherits BaseModel class'''
    state_id = ""
    name = ""
