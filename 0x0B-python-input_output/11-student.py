#!/usr/bin/python3
"""Class student"""

class Student:
    """the main class"""
    def __init__(self, first_name, last_name, age):
        """the public instance attributes
        Args:
            first_name:the first name of student
            last_name: last name
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name= last_name
        self.age = age
    def to_json(self, attrs=None):
        """the public method to retrieve the dictionary"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self,json):
        """to replace the attributes of the student"""
        for k, x in json.items():
            setatter(self, k, x)
