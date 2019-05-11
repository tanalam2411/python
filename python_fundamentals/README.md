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
with open('http://xyz.com/f/txt') as f:
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

