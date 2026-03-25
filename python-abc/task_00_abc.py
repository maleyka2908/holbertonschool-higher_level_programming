#!/usr/bin/python3
"""
This module defines an abstract base class Animal and its subclasses
Dog and Cat to demonstrate Abstract Base Classes (ABC) in Python.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        to return the specific sound of the animal.
        """
        pass


class Dog(Animal):
    """Subclass of Animal representing a Dog."""

    def sound(self):
        """Returns the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass of Animal representing a Cat."""

    def sound(self):
        """Returns the sound made by a cat."""
        return "Meow"
