#!/bin/python

import sys


# n = int(raw_input().strip())
# c = raw_input()

n = 10
c = '10 20 20 10 10 30 50 10 20'

print 1<=n<=100

if 1<=n<=100:
    
    keys = set(c)
    
    my_dict = dict()
    
    ci_list = c.strip().split()
    
    for each in ci_list:
        if each not in my_dict:
            my_dict[each] = 0
        my_dict[each] = my_dict[each] + 1
    
    total = 0
    
    for i in my_dict.values():
        total = total + i/2
        
    print total