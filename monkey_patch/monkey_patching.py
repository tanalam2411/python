#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Monkey patching is a way of programming in which we can modify or extend the
executing code at runtime.

Monkey patching is useful for testing purpose not suitable for production
environment.

Below we are considering an example in which we are trying to monkey patch
get_data method of class BaseClass from base_module.
"""


from base_module import BaseClass


def monkey_bar(self):
    return [100, 200, 300]

inst_1 = BaseClass()
data_1 = inst_1.get_data()
print inst_1.return_total(data_1)


BaseClass.get_data = monkey_bar
inst_2 = BaseClass()
data_2 = inst_2.get_data()
print inst_2.return_total(data_2)

