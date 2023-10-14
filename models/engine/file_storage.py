#!/usr/bin/python3
"""
FileStorage class for serializing and deserializing instances to/from a JSON file.
"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    FileStorage class defines methods for managing object serialization and deserialization to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Retrieve all objects from the storage, or filter by class if cls is provided.
        Args:
            cls (class): Class to filter objects by.
        Returns:
            A dictionary of all objects or objects of the specified class.
        """
        if cls is None:
            return FileStorage.__objects
        filtered_objects = {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}
        return filtered_objects

    def new(self, obj):
        """
        Add a new object to the storage.
        Args:
            obj: The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize objects to a JSON file.
        """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize objects from the JSON file.
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = models[class_name]
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance

# Add the new classes to the models dictionary
models = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}
