"""
    Implementation of sigma function
"""


def sigma(begin, end, func: [], inc=1):
    """
    :param begin: start value (inclusive)
    :param end: terminating value (inclusive)
    :param func: function to sum
    :param inc: increment value
    :return: The sum of func return values on range begin -> end (inclusive)
    """
    res = 0
    while begin <= end:
        res += func(begin)
        begin += inc

    return res

