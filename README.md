# Function-Chain-Python

[![Build Status](https://travis-ci.org/Thoxvi/Function-Chain-Python.svg?branch=master)](https://travis-ci.org/Thoxvi/Function-Chain-Python) [![PyPI](https://img.shields.io/pypi/v/fc.svg)](https://pypi.python.org/pypi/fc)

Enables Python to be functionally chain-styled.

## Document

- **Simplified Chinese documents** **[here](./docs/zh-CN/main/README.md)**.

If you are interested in me,you can follow my [Blog](https://blog.thoxvi.com/2018/05/17/Fuck%E8%BF%99%E4%B8%AA%E4%B8%96%E7%95%8C%E4%B8%8D%E5%A4%9F%E5%A5%BD%E7%9A%84%E4%B8%9C%E8%A5%BF/)(~~一波软广2333~~)。

## How to use?

install form pypi

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
    .filter(lambda x: x > 4)
    .print()
    # [5, 6]
    .map(lambda x: x + 1)
    .done()
)
assert l == [6, 7]
```

You can check this this [test file](./tests/test_fc.py) and understand more

## Have Fun ;)
