#!/usr/bin/python3
"""
This module contains a function to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data = []
        # CSV faylını oxuyuruq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # DictReader hər sətri avtomatik lüğətə çevirir
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        # Məlumatı data.json faylına yazırıq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
