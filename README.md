# Fuck-Py-Functional

[![Build Status](https://travis-ci.org/Thoxvi/Fuck-Py-Functional.svg?branch=master)](https://travis-ci.org/Thoxvi/Fuck-Py-Functional)

Enables Python to be functionally chain-styled.

## How to use?

install form pypi

`$ pip install fc`

and you just import `Fc`,like this: `from fc import Fc`

then you can enjoy lambda like JS:

```python
from fc import Fc

l = [1, 2, 3, 4, 5, 6, 7]

# Map
ml = Fc(l).map(lambda x: x + 1).done()
# ml == [2, 3, 4, 5, 6, 7, 8]

# Filter
ml = Fc(l).filter(lambda x: x > 3).filter(lambda x: x < 6).done()
# ml == [4, 5]

# Resort
ml = Fc(l).resort().done()
# ml == [7, 6, 5, 4, 3, 2, 1]

# Sort
ml = Fc(ml).sort().done()
# ml = [1, 2, 3, 4, 5, 6, 7]

# Reduce
result = Fc(l).reduce(lambda x, y: x + y)
# result == 28

# Len
mll = Fc(l).len()
# mll == 0

# and...

l = [1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).map(lambda x: x + 1).filter(lambda x: x > 6).resort().done()
# ml == [7, 8]
```

You can check this this [test file](./tests/test_fc.py) and understand more

## Have Fun ;)