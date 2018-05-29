Function-Chain-Python
=====================

`Build Status`_ `PyPI`_

Enables Python to be functionally chain-styled.

Document
--------

-  **Simplified Chinese documents** `here`_.

If you are interested in me,you can follow my
`Blog`_\ ([STRIKEOUT:一波软广2333])。

How to use?
-----------

install form pypi:

::

   $ pip install fc

and you just import ``Fc``,like this: ``from fc import Fc``

then you can enjoy lambda like Kotlin/JS:

.. code:: python

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

You can check this this `test file`_ and understand more.

Have Fun ;)
-----------

.. _Build Status: https://travis-ci.org/Thoxvi/Function-Chain-Python
.. _PyPI: https://pypi.python.org/pypi/fc
.. _here: ./docs/zh-CN/main/README.md
.. _Blog: https://blog.thoxvi.com/2018/05/17/Fuck%E8%BF%99%E4%B8%AA%E4%B8%96%E7%95%8C%E4%B8%8D%E5%A4%9F%E5%A5%BD%E7%9A%84%E4%B8%9C%E8%A5%BF/
.. _test file: ./tests/test_fc.py