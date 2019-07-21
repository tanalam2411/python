#! /usr/bin/env python


"""
Bubble sort implementation in Python.

Input array = [5, 4, 3, 2, 1]

- Ascending order

In every iteration one of the largest number will be shifted to the end.

So it will take N - 1 iteration if array is completely unsorted, meaning is
case if we're doing asce order the input order would be in des order and vice
versa.


"""



input_array = [5, 4, 3, 2, 1]


for i in range(len(input_array) - 1):
    print 'i: ', i
    print '-------'
    for j in range(1, len(input_array) - i):

        num1 = input_array[j-1]
        num2 = input_array[j]

        if num2 < num1:
            input_array[j-1], input_array[j] = input_array[j], input_array[j-1]

        print 'j: ', j

    print '-------'

print input_array



