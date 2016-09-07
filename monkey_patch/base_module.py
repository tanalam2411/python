#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseClass(object):
    def __init__(self):
        pass

    def get_data(self):
        """
        Consider this method is returning data fetched by doing some DB query or
        some rest call.
        """
        return [10, 20, 30]

    def return_total(self, data):
        return sum(data)
