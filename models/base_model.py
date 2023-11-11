#!/usr/bin/python3
""" Module creates a BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel Class
    """
    def __init__(self,*args,**kwargs):
        """ defines common attributes of objects
        """
        self.id=str(uuid.uuid4())
        self.created_at=datetime.now()
        self.updated_at=datetime.now()

    def __str__(self):
        """returns class name, id, attribute dictionary
        """
        class_name="["+ self.__class__.__name__+"]"
        return class_name + " (" + self.id + ") " +str(self.__dict__)

    def save(self):
         """ updates time
         """
         self.updated_at=datetime.now()

    def to_dict(self):
        """ Returns dictionary representation of object
        """
        new_dict={}
        for i, j in self.__dict__.items():
            if i== "created_at" or i =="updated_at":
                new_dict[i]=j.isoformat()
            else:
                new_dict[i]=j
        new_dict['__class__']=self.__class__.__name__
        return new_dict

