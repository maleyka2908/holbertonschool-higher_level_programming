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
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Prints area and perimeter of any object with those methods."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
