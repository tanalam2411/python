#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
default log level is warning.
https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
"""
import logging
path = "/home/tan/tanveer/github/python/python_logging/test.log"


def basic_logging():
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG)
    logging.debug("Debug message.")
    logging.info("Info message.")
    logging.warning("Warning message.")
    logging.critical("Ciritical message.")
    logging.debug("%s is running at line number %d.", 'Tan logging', 13)


def change_msg_format():
    "https://docs.python.org/2/library/logging.html#logrecord-attributes"
    logging.basicConfig(format="%(levelname)s:%(message)s", filename=path, filemode='w', level=logging.DEBUG)
    logging.debug("Formatted message.")
    logging.info("Informative message.")


def display_datetime():
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.debug("is when event occurred.")


def datetime_format():
    """
    09/19/2016 08:04:52 PM formatted time.
    :return:
    """
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('formatted time.')

# basestring()
# change_msg_format()
# display_datetime()
# datetime_format()