#!/usr/bin/python3
"""
This module demonstrates the use of mixins in Python.
It defines SwimMixin, FlyMixin, and a Dragon class that uses both.
"""


class SwimMixin:
    """Mixin class to add swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits swimming and flying abilities from mixins.
    """

    def roar(self):
        """Prints a roaring message unique to the dragon."""
        print("The dragon roars!")
