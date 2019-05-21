1 ) Strongly types language

Every object has a type

```python
>>> x = [1, 2, 3]
>>> type(x)
<class 'list'>
```

2 ) Dynamically typed language

No type checking prior to running it.

3 ) Duck typing - Object type is determined at run time.

4 ) Zen of Python

```python
import this
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


5 ) REPL - Read, Evaluate, Print, Loop

6 ) Scalar types - int

int - unlimited precision signed integer(+-)

```python
# Decimal
>>>10
10

# Binary
>>> 0b10
2

# Octal
>>> 0o10
8

# Hex
>>> 0x10
16
``` 

7 ) Scalar type - float

e or E is - 10 to the power next to e or E
```python
>>> 3e8
300000000.0

>>> 3.125E7
31250000.0

>>> 3.125*(10**7)
31250000.0
```

```python
# nan - not a number
>>> float('nan')
nan
>>> type(float('nan'))
<type 'float'>

# positive infinity
>>> float('inf')
inf

# negative infinity
>>> float('-inf')
-inf

```


8 ) Collection type - dict

9 ) 
```python
from urllib.request import urlopen
with urlopen('http://xyz.com/f/t.txt') as f:
    words = []
    
    for line in f:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            words.append(word)

```

10 ) Python 3 source encoding default is utf-8

11 ) bytes in a sequence of bytes, str is a sequence of Unicode codepoints

12 ) Use encode and decode method to convert from str <-> bytes

13 ) Doc string
```python
"""
Module level Documentation.
"""

def func(url):
    """Function level doc
    
    Args:
        url: Some url
    """
```

```python
Module level Documentation.

Function level doc
    
    Args:
        url: Some url
```

14 ) Cmd lib - argparse, docopt

15 ) Tuple unpacking
```python
>>> (a, (b, (c, d))) = (1, (2, (3, 4)))
>>> a
1
>>> b
2
>>> c
3
>>> d
4

```

16 ) Str partition
```python
>>> a, b, c = 'a-b'.partition('-')
>>> a
'a'
>>> b
'-'
>>> c
'b'

```

17 ) Set - Unordered collection of unique, immutable objects
```python

>>> s = {1, 2, 3}
>>> s.add(4)
>>> s
set([1, 2, 3, 4])
>>> s.update([5, 6, 7])
>>> s
set([1, 2, 3, 4, 5, 6, 7])
>>> 
>>> s.discard(5)
>>> s
set([1, 2, 3, 4, 6, 7])
>>> s.discard(5)
>>> s
set([1, 2, 3, 4, 6, 7])
>>> 

```

Union : Unique elements from both the sets
```python
>>> s1 = {1, 2, 3}
>>> s2 = {3, 4, 5}
>>> s1.union(s2)
set([1, 2, 3, 4, 5])
>>> s2.union(s1)
set([1, 2, 3, 4, 5])

```

Intersection: Common in both the sets
```python
>>> s1.intersection(s2)
set([3])

```

Difference : Not present in the other set
```python
>>> s1.difference(s2)
set([1, 2])
>>> s2.difference(s1)
set([4, 5])
```

Symmetric Difference - Present in Set1 and Set2 but not in both
```python
>>> s1.symmetric_difference(s2)
set([1, 2, 4, 5])
>>> s2.symmetric_difference(s1)
set([1, 2, 4, 5])

```

Subset - all elements of setA exists in setB
```python
>>> {1, 2}.issubset(s1)
True

```

Superset - setA contains all elements of setB
```python
>>> s1.issuperset({1, 2})
True

```

Disjoint - no common elements between setA and setB
```python
set([1, 2, 3])
>>> s1.isdisjoint({4, 5})
True

```


18 ) Difference between iterable and sequence - both are interable but sequence are ordered and interable may or maynot be ordered. 
     Dict is not a sequence. 
     
     
19 ) Passing print msg to stderr
```python
>>> import sys
>>> 
>>> try:
...     f = open('/a/b/c.txt')
... except IOError as e:
...     print(e, file=sys.stderr)
... 
[Errno 2] No such file or directory: '/a/b/c.txt'
>>> 

```


20 ) List and Set Comprehension -
```python
>>> from math import factorial
>>> f = [len(str(factorial(x))) for x in range(20)]
>>> f
[1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
>>> 
>>> f = {len(str(factorial(x))) for x in range(20)}
>>> f
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
>>> 
```

21 ) Dict Comprehension - 
```python
>>> import os
>>> import glob
>>> file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
>>> file_sizes
{'/home/tan/tanveer/git_python/python/__init__.py': 0}

```


22 ) Prime number - 
```python

>>> from math import sqrt
>>> def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True    

>>> {i: is_prime(i) for i in range(100)}
```

23 ) Iterable protocol - Iterable objects can be passed to the built-in `iter()` function to get an interator.

`iterator = iter(iterable)`

Iterator protocol - Iterator objects can be passed to the build-in `next()` function to fetch the next item.

`item = next(iterator)`

```python
>>> l = [1,2,3]
>>> i = iter(l)
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

```


24 ) Generator - At a glance, the yield statement is used to define generators, replacing the return of a function to provide a result to its caller without destroying local variables. Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off.
```python
def take(count, iterable):

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]

    for item in take(3, items):
        print(item)

run_take()

---
2
4
6
---


```

















------------------------------------------------
1) http://book.pythontips.com/en/latest/index.html