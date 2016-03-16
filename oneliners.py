"""Module to hold short functions, mainly for readability in programs."""
import numpy as np

def unzip(multi_dim_array):
    """
    Return unpacked elements of multi dimentional list packed as tuples.

    return zip(*multi_dim_array)
    """
    return zip(*multi_dim_array)


def unique(duplicate_list):
    """
    Return all unique elements in a list.

    return list(set(duplicate_list))
    """
    return list(set(duplicate_list))


def flatten(multi_dim_array):
    """
    Return flattened list

    return np.array(multi_dim_array).flatten()
    """
    print 'broken'
    return list(np.array(multi_dim_array).flatten())
