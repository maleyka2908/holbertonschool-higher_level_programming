#!/usr/bin/python3
"""
Module for Shape, Circle, Rectangle and shape_info function.
Demonstrates ABC and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Prints area and perimeter of any object with those methods."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
