#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://docs.python.org/3/howto/sockets.html

socket.AF_INET - ipv4
socket.SOCK_STREAM - tcp
"""


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
print s.getsockname()
s.close()