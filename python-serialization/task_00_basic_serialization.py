#!/usr/bin/python3
"""
Basic serialization module.

This module provides functions to serialize Python dictionaries to JSON files
and deserialize JSON files back to Python dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): A Python Dictionary with data to serialize
        filename (str): The filename of the output JSON file.
                       If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

