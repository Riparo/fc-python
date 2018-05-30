# Function-Chain-Python

[![Build Status](https://travis-ci.org/Thoxvi/Function-Chain-Python.svg?branch=master)](https://travis-ci.org/Thoxvi/Function-Chain-Python) [![PyPI](https://img.shields.io/pypi/v/fc.svg)](https://pypi.python.org/pypi/fc)

Enables Python to be functionally chain-styled.

## Document

- **Simplified Chinese documents** **[here](./docs/zh-CN/main/README.md)**.

If you are interested in me,you can follow my [Blog](https://blog.thoxvi.com/2018/05/17/Fuck%E8%BF%99%E4%B8%AA%E4%B8%96%E7%95%8C%E4%B8%8D%E5%A4%9F%E5%A5%BD%E7%9A%84%E4%B8%9C%E8%A5%BF/)(~~一波软广2333~~)。

## How to use?

install form pypi:

```
$ pip install fc
```

and you just import `Fc`,like this: `from fc import Fc`

then you can enjoy lambda like Kotlin/JS:

```python
from fc import Fc

l = (
  Fc([1, 2, 3, 4, 5])
    .map(lambda x: x + 1)
    .filter(lambda x: x > 4).print()    # [5, 6]
    .map(lambda x: x + 1).print()       # [6, 7]
    .cat([8, 9]).print()                # [6, 7, 8, 9]
    .add(10).print()                    # [6, 7, 8, 9, 10]
    .catHead([1, 2, 3, 4, 5]).print()   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    .limit(3)
    .done()
)
assert l == [1, 2, 3]
```

## Multi-line Lambda

if you not like single line lambda for python,you can import `mml`(`Make Multi-line Lambda`) of `fc` like this:

```Python
from fc import Fc
from fc import mml as m

# normal
assert Fc([1, 2, 3]).map(m(
  '''
    lambda x:
      x*=2
      return x
  '''
)).done() == [2, 4, 6]

# default value
assert Fc([1, 2, 3]).map(m(
  '''
    lambda x,y=1:
      x+=y
      return x
  '''
)).done() == [2, 3, 4]

# support list,dict
assert m(
  '''
      lambda *l,**k:
        return (l,k)
    '''
)(1, a=2) == ((1,), {'a': 2})

# even supports recursive anonymous functions(but must use {self})
assert Fc([1, 2, 3, 4, 5]).map(m('''
lambda x:
  if x<=0: return 0
  else:    return x+{self}(x-1)
  ''')).done() == [1, 3, 6, 10, 15]

```

## More

You can check this this [test file](./tests/test_fc.py) and understand more.

## Have Fun ;)
