
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

