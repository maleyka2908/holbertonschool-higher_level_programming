#!/usr/bin/python3
"""
This module contains functions to serialize and deserialize
dictionaries using XML format.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: A dictionary containing the data from the XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # XML-dən lüğəti yenidən qururuq
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except FileNotFoundError:
        return None
    except Exception:
        return None
