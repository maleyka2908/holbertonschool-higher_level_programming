#!/usr/bin/python3
"""
This module provides a function that indents text.
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of '.', '?' and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Xüsusi simvollar
    special_chars = ".?:"

    i = 0
    # Mətnin əvvəlindəki boşluqları təmizləyirik
    text = text.strip(" ")

    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            # Simvoldan sonra gələn boşluqları keçirik
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
