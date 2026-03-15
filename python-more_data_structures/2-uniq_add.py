#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    """
    # Siyahını 'set'ə çeviririk ki, dublikatlar silinsin
    unique_numbers = set(my_list)

    # Unikal rəqəmlərin cəmini hesablayıb qaytarırıq
    return sum(unique_numbers)
