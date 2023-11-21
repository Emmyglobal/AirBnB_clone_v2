#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
	"""
		Class for handling JSON serialization and deserialization
		"""

		__file_path = "file.json"
		__objects = {}

		def all(self, cls=None):
			"""Returns a dictionary of objects"""
				if cls is None:
				return FileStorage.__objects
				return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

				def new(self, obj):
					"""Sets in __objects the obj with key <obj class name>.id"""
						key = "{}.{}".format(type(obj).__name__, obj.id)
						FileStorage.__objects[key] = obj

						def save(self):
							"""Serializes __objects to the JSON file (path: __file_path)"""
								temp = {}
								for key, val in FileStorage.__objects.items():
									temp[key] = val.to_dict()
									with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
										json.dump(temp, f)

										def reload(self):
											"""Loads storage dictionary from file"""
												classes = {
													'BaseModel': BaseModel, 'User': User, 'Place': Place,
													'State': State, 'City': City, 'Amenity': Amenity,
													'Review': Review
												}
try:
temp = {}
with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
temp = json.load(f)
	for key, val in temp.items():
	cls_name = val['__class__']
	self.all()[key] = classes[cls_name](**val)
	except FileNotFoundError:
		pass

		def delete(self, obj=None):
			"""Deletes obj from __objects if it exists"""
				if obj is not None:
				key = "{}.{}".format(type(obj).__name__, obj.id)
				if key in FileStorage.__objects:
				del FileStorage.__objects[key]

