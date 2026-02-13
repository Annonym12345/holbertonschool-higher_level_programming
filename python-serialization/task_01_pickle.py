#!/usr/bin/python3
"""
Custom object serialization module using pickle.

This module provides a CustomObject class that can serialize and deserialize
itself using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class to demonstrate pickle serialization.

    Attributes:
        name (str): The name of the object
        age (int): The age value
        is_student (bool): Whether the object represents a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the object
            age (int): The age value
            is_student (bool): Whether the object represents a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object

        Returns:
            None if an error occurs, otherwise nothing
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
