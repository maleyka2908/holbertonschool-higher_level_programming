#!/usr/bin/python3
"""
This module defines the CountedIterator class.
It wraps an iterator and keeps track of the number of items iterated.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items fetched.
    """

    def __init__(self, data):
        """
        Initializes the iterator and the counter.

        Args:
            data: An iterable to be converted into an iterator.
        """
        self.iterator = iter(data)
        self.count = 0

    def get_count(self):
        """Returns the current number of items iterated."""
        return self.count

    def __next__(self):
        """
        Increments the counter and returns the next item.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
