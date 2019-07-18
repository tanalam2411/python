

"""
https://docs.python.org/3/library/abc.html
https://pymotw.com/3/abc/
"""

from abc import ABCMeta

class BaseClass(object):
    """
    Python 2
    declare - magic attribute
        __metaclass__ = ABCMeta

    Python 3

    class Name(metaclass=ABCMeta):
    """
    __metaclass__ = ABCMeta

