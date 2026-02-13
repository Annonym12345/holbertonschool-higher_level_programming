#!/usr/bin/python3
"""
XML serialization and deserialization module.

This module provides functionality to serialize Python dictionaries to XML
and deserialize XML files back to Python dictionaries.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data

    Returns:
        None
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate through the dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Add indentation for pretty printing
    ET.indent(root, space='    ')

    # Create an ElementTree object and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The filename of the XML file to deserialize

    Returns:
        dict: The deserialized Python dictionary
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct the dictionary
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
