#!/usr/bin/python3
""" Initialization module for the HBNB project's data models. """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
