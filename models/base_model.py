#!/usr/bin/python3
"""This module defines the baseclass"""
from datetime import datetime
import uuid


class BaseModel:
    """This is the base class for all classes in this project"""
    def __init__(self, *args, **kwargs):
        """Is the class constructor"""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        fval = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, fval)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return dictionary representation of class"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute when called"""
        from models import storage

        storage.save()
        self.update_at = datetime.now()

    def to_dict(self):
        """Coverts an object to a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
