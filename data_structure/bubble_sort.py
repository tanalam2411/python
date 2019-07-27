#! /usr/bin/env python


"""
Bubble sort implementation in Python.

Input array = [5, 4, 3, 2, 1]

- Ascending order

In every iteration one of the largest number will be shifted to the end.

So it will take N - 1 iteration if array is completely unsorted, meaning in
case if we're sorting in asc order and the input order would be in des order and
vice versa.

e.g:

arr  = [5, 4, 3, 2, 1]

1st Iteration:
    Compare : arr[0] > arr[1]
            if True than Swap arr[0], arr[1] = arr[1], arr[0]
    Compare : arr[1] > arr[2]
            if True than Swap arr[1], arr[2] = arr[2], arr[1]
    Repeat till arr[N-1] > arr[N]

2nd Iteration:
    Compare : arr[0] > arr[1]
            if True than Swap arr[0], arr[1] = arr[1], arr[0]
    Repeat till arr[N-2] > arr[N-1]  # As the last number is already sorted

N-1 Iteration:
    Compare : arr[0] > arr[1]
            if True than Swap arr[0], arr[1] = arr[1], arr[0]
            break

Time complexity:
    Best Case  -
    Avg Case   -
    Worst Case -

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



