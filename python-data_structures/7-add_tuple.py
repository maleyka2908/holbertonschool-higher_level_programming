#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples by their first two elements."""
    # Hər iki tuple-ı ən azı 2 elementi olacaq şəkildə genişləndiririk
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # İlk iki elementin cəmindən yeni tuple yaradırıq
    return (a[0] + b[0], a[1] + b[1])
