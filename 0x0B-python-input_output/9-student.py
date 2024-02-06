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
    def to_json(self):
        """the dictionary rep of the student"""
        return self.__dict__