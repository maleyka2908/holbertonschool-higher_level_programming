#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    """
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
