#! -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class ConnectionFactory(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        """
        :return:
        """

    def get_connection(self):
        pass

    def __enter__(self):
        """
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """


class Test:

    _ins = None

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit')

    def __new__(cls, *args, **kwargs):
        if cls._ins is None:
            cls._ins = super(Test, cls).__new__(cls, *args, **kwargs)
        return cls._ins

    def __init__(self, num):
        self.num = num
        print('init')




with Test(1) as a:
    pass

