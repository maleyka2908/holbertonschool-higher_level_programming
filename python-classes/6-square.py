#!/usr/bin/python3
"""
This module defines a Square class with size and position validation.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Returns the square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character taking position into account.
        """
        if self.__size == 0:
            print("")
            return

        # Handle vertical position (position[1])
        if self.__size_position[1] > 0:
            for _ in range(self.__size_position[1]):
                print("")

        # Handle horizontal position and printing of the square
        for _ in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
EOFcat << EOF > 6-square.py
#!/usr/bin/python3
"""
This module defines a Square class with size and position validation.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Returns the square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character taking position into account.
        """
        if self.__size == 0:
            print("")
            return

        # Handle vertical position (position[1])
        if self.__size_position[1] > 0:
            for _ in range(self.__size_position[1]):
                print("")

        # Handle horizontal position and printing of the square
        for _ in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
