
import operator
from itertools import *


# print list(itertools.cycle([1, 2, 3]))


def itertool_chain():
    """
    Accepts multiple iterable and return a single sequence as if all items
    belongs to that sequence.
    """
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7, 8]

    print(list(chain(l1, l2)))

    """
    [1, 2, 3, 4, 5, 6, 7, 8]
    """


def islice_and_count():
    """
    count(start=0, step=1) --> count object
    Return a count object whose .next() method returns consecutive values.

    islice(iterable, [start,] stop [, step]) --> islice object
    """
    print(list(islice(count(), 5, 50, 10)))
    """
    [5, 15, 25, 35, 45]
    """


def tee_count():
    """
    Can make multiple clone of a sequence.
    Note: The original sequence cannot be used once cloned
    """
    single_iterator = islice(count(), 0, 5)
    clone1, clone2, clone3 = tee(single_iterator, 3)
    print list(clone1), list(clone2), list(clone3)
    print list(single_iterator)

    """
    [0, 1, 2, 3, 4] [0, 1, 2, 3, 4] [0, 1, 2, 3, 4]
    []
    """


def cycle_items():
    count = 0
    for item in cycle(['a', 'b', 'c']):
        print item,

        count += 1
        if count > 8:
            break

    """
    a b c a b c a b c
    """


def accumulate_data():

    # available from python3 onwards

    # result = itertools.accumulate(range(5))
    # print list(result)
    """
    0, 1+0, 2+1, 3+3, 4+6
    [0, 1, 3, 6, 10]
    """

    # result = accumulate(range(1, 5), operator.mul)
    # print list(result)

    """
    1, 2*1, 3*2, 4*6
    [1, 2, 6, 24]
    """


def dropwhile_data():
    """
    Filters items until condition becomes False
    """
    data = dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])
    print list(data)

    """
    [5, 6]
    """


def takewhile_data():
    """
    Filters items until condition becomes True
    :return:
    """
    data = takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])
    print list(data)

    """
    [[1, 2, 3, 4]
    """


def combination_data():

    data = combinations('ABCD', 3)
    for i in data:
        print i

    """
    # Sequence - 2
    ('A', 'B')
    ('A', 'C')
    ('A', 'D')
    ('B', 'C')
    ('B', 'D')
    ('C', 'D')
    
    # Sequence - 3
    ('A', 'B', 'C')
    ('A', 'B', 'D')
    ('A', 'C', 'D')
    ('B', 'C', 'D')
    """


def combination_with_replacement_data():

    data = combinations_with_replacement('ABCD', 2)
    for i in data:
        print i

    """
    # Sequence - 2
    ('A', 'A')
    ('A', 'B')
    ('A', 'C')
    ('A', 'D')
    ('B', 'B')
    ('B', 'C')
    ('B', 'D')
    ('C', 'C')
    ('C', 'D')
    ('D', 'D')
    """


def compress_data():

    filtered = [True, False, False, True, True]
    to_fillter = 'ABCDEFGHI'
    data = compress(to_fillter, filtered)
    print data


any
if __name__ == '__main__':

    # itertool_chain()
    # islice_and_count()
    # tee_count()
    # cycle_items()
    # accumulate_data()
    # dropwhile_data()
    # takewhile_data()
    # combination_data()
    combination_with_replacement_data()