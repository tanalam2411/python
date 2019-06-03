
1 ) Packages - 

Both package and module's type is 'module'

```python

>>> import urllib
>>> import urllib.request
>>> type(urllib)
<class 'module'>
>>> type(urllib.request)
<class 'module'>
>>> urllib.__path__
['/home/tan/anaconda3/lib/python3.6/urllib']
>>> urllib.request.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'urllib.request' has no attribute '__path__'


```

2 ) __ _all_ __ - Include in __ _init_ __.py module to limit what needs to be imported in case of importing 'from module import *'

```python
__all__ = ['func_1', 'func_2']
```


3 ) Namespace packages - Split packages across several directories.

Useful for splitting large packages into multiple parts.

While looking for a module or package named "foo", for each directory in the parent path:

- If <directory>/foo/__init__.py is found, a regular package is imported and returned.
- If not, but <directory>/foo.{py,pyc,so,pyd} is found, a module is imported and returned. The exact list of extension varies by platform and whether the -O flag is specified. The list here is representative.
- If not, but <directory>/foo is found and is a directory, it is recorded and the scan continues with the next directory in the parent path.
- Otherwise the scan continues with the next directory in the parent path.

Differences between namespace packages and regular packages

- Portions of namespace packages need not all come from the same directory structure, or even from the same loader. Regular packages are self-contained: all parts live in the same directory hierarchy.
- Namespace packages have no __file__ attribute.
- Namespace packages' __path__ attribute is a read-only iterable of strings, which is automatically updated when the parent path is modified.
- Namespace packages have no __init__.py module. To avoid package level initialization.
- Namespace packages have a different type of object for their __loader__ attribute.


```bash
.
├── Lib
│   └── test
│       └── namespace_pkgs
│           ├── project1
│           │   └── parent
│           │       └── child
│           │           ├── one.py
│           │           └── __pycache__
│           │               └── one.cpython-36.pyc
│           └── project2
│               └── parent
│                   └── child
│                       ├── __pycache__
│                       │   └── two.cpython-36.pyc
│                       └── two.py

```

```python
>>> import sys
>>> sys.path += ['Lib/test/namespace_pkgs/project1', 'Lib/test/namespace_pkgs/project2']
>>> import parent.child.one
>>> parent.child.one.__file__
'Lib/test/namespace_pkgs/project1/parent/child/one.py'
>>> parent.__path__
_NamespacePath(['Lib/test/namespace_pkgs/project1/parent', 'Lib/test/namespace_pkgs/project2/parent'])
>>> parent.child.__path__
_NamespacePath(['Lib/test/namespace_pkgs/project1/parent/child', 'Lib/test/namespace_pkgs/project2/parent/child'])
>>> import parent.child.two
>>> parent.child.two.__file__
'Lib/test/namespace_pkgs/project2/parent/child/two.py'

```


* __ _pycache_ __ - To speed up loading modules, Python caches the compiled version of each module in the __ _pycache_ __ directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.6 the compiled version of spam.py would be cached as __ _pycache_ __/spam.cpython-36.pyc.

4 ) Executable directories (__ _main_ __)- Directories containing an entry point for Python execution.

```bash
└── reader
    ├── __main__.py
    ├── __pycache__
    │   └── __main__.cpython-36.pyc
    └── reader
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-36.pyc
        │   └── reader.cpython-36.pyc
        └── reader.py

```

Now you can run package itself.

```bash
# This will call __main__ module from reader package
$  python3 reader $filename
```

5 ) Recommended project struture

```bash
project_name/
├── __main__.py
├── project_name
│   ├── __init__.py
│   ├── more_source.py
│   ├── subpackage1
│   │   └── __init__.py
│   └── test
│       ├── __init__.py
│       └── test_code.py
└── setup.py

```

6 ) sys.path[0] - Import modules from the current directory

```python
>>> import sys
>>> sys.path[0]
''

```

7 ) -m - Modules can be executed by passing -m argument
```bash
$ python3 -m p1
```

8 ) Positional, keyword argument - 

```python
# arg1 - positional arg
# arg2 - keyword arg
# 1.1 - default argument value
function_name(arg1, arg2=1.1)
```

9 ) __ _call_ __() - Callable instances

```python
class A:

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('A: %s' % self.name)


obj = A('Python')
obj()


--------------------
A: Python
--------------------

```

10 ) Detecting callable Objects:

```python
>>> def is_even(x): return x % 2 == 0
... 
>>> callable(is_even)
True
>>> is_odd = lambda x: x % 2 != 0
>>> callable(is_odd)
True
>>> callable(list)
True
>>> callable(list.append)
True
>>> class CallMe:
...     def __call__(self):
...         print('called!!!')
... 
>>> call_me = CallMe()
>>> callable(call_me)
True
>>> 
>>> callable('abcdef')
False
```

11 ) *args - 

```python
def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    print i, v

    for length in i:
        v *= length
    return v


print hypervolume(2, 4)
print hypervolume(2, 4, 6)
print hypervolume(2, 4, 6, 8)
print hypervolume(1)

-------------------------------------------
<tupleiterator object at 0x7f800913cb90> 2
8
<tupleiterator object at 0x7f800913cb90> 2
48
<tupleiterator object at 0x7f800913cb90> 2
384
<tupleiterator object at 0x7f800913cb90> 1
1
-------------------------------------------

```

*args unpacking
```python
def print_args(a1, a2, *args):
    print(a1)
    print(a2)
    print(args)

t = (1, 2, 3, 4)
print_args(*t)


--------
1
2
(3, 4)
--------
```

same goes for **kwargs

```python
def print_kwargs(k1, k2, **kwargs):
    print(k1)
    print(k2)
    print(kwargs)

d = dict(k1=1, k2=2, k3=3, k4=4)
print_kwargs(**d)

---------------------
1
2
{'k3': 3, 'k4': 4}
---------------------

```

12 ) *zip - 

```python
>>> l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> 
>>> for item in zip(l[0], l[1], l[2]): print item
... 
(1, 4, 7)
(2, 5, 8)
(3, 6, 9)
>>> 
>>> 
>>> for item in zip(*l): print item
... 
(1, 4, 7)
(2, 5, 8)
(3, 6, 9)

>>> list(zip(*l))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

```


13 ) [Closures](https://www.programiz.com/python-programming/closure) - A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.


These non-local variables are read only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.
```python
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()

--------------------
Inner function:  10
Outer function:  10
--------------------
``` 


```python
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")
```

**Defining a Closure Function** - 
In the example above, what would happen if the last line of the function print_msg() returned the printer() function instead of calling it? This means the function was defined as follows.

```python
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
```

The print_msg() function was called with the string "Hello" and the returned function was bound to the name another. On calling another(), the message was still remembered although we had already finished executing the print_msg() function.

This technique by which some data ("Hello") gets attached to the code is called closure in Python.

This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

Try running the following in the Python shell to see the output.

```python
>>> del print_msg
>>> another()
Hello
>>> print_msg("Hello")
Traceback (most recent call last):
...
NameError: name 'print_msg' is not defined
```


14 ) Function Factories - Function that returns new, specialized functions.

```python
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
print(square.__closure__)
print "cell_contents: ", square.__closure__[0].cell_contents
print(square(2))
print(square(5))

qube = raise_to(3)
print "cell_contents: ", qube.__closure__[0].cell_contents
print(qube(3))
print(qube(4))

----
(<cell at 0x7f9e3689f0c0: int object at 0x2508140>,)
cell_contents:  2
4
25
cell_contents:  3
27
64
----

```

15 ) Nonlocal keyword - Introduce names from enclosing namespace into the local namespace.