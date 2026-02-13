#!/usr/bin/python3
"""
CSV to JSON conversion module.

This module provides functionality to convert CSV files to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and write it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to convert

    Returns:
        bool: True if the conversion was successful, False otherwise
    """
    try:
        # Read the CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Use DictReader to convert each row into a dictionary
            csv_reader = csv.DictReader(csv_file)
            # Convert to a list of dictionaries
            data = list(csv_reader)

        # Write the JSON data to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
