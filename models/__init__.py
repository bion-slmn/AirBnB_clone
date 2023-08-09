#!/usr/bin/python3
''' creating an instance of FileStorage classs and calling reload'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
