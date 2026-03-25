#!/usr/bin/python3
"""
This module explores multiple inheritance by defining Fish and Bird classes,
and a FlyingFish class that inherits from both.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints fish swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat message."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints bird flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Overrides fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")
