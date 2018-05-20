from functools import reduce
from collections import Iterable
from types import FunctionType


class FcTypeError(Exception):
  pass


class FcRangeError(Exception):
  pass


class Fc:
  '''
  FunctionChain
  '''

  def __init__(self, mylist):
    if not isinstance(mylist, Iterable):
      raise FcTypeError(str(list) + " is Not Iterable")
    self.__mylist = mylist

  def map(self, func):
    if not isinstance(func, FunctionType):
      raise FcTypeError(str(func) + " is Not Function")
    return Fc(map(func, self.__mylist))

  def filter(self, func):
    if not isinstance(func, FunctionType):
      raise FcTypeError(str(func) + " is Not Function")
    return Fc(filter(func, self.__mylist))

  def sort(self, func=None):
    if func is None:
      return Fc(list(sorted(self.__mylist)))
    else:
      if not isinstance(func, FunctionType):
        raise FcTypeError(str(func) + " is Not Function")
      return Fc(list(sorted(self.__mylist, key=func)))

  def resort(self, func=None):
    if func is None:
      return Fc(sorted(self.__mylist, reverse=True))
    else:
      if not isinstance(func, FunctionType):
        raise FcTypeError(str(func) + " is Not Function")
      return Fc(sorted(self.__mylist, key=func, reverse=True))

  def getAfter(self, start, count=-1):
    if start < 0:
      start = 0
    c1 = 0
    c2 = 0
    newlist = []
    for it in self.__mylist:
      if c1 >= start:
        if c2 >= count and count != -1:
          break
        else:
          newlist.append(it)
          c2 += 1
      c1 += 1
    return Fc(newlist)

  def skip(self, count):
    if count <= 0:
      return self
    c1 = 0
    newlist = []
    for it in self.__mylist:
      if c1 >= count:
        newlist.append(it)
      c1 += 1
    return Fc(newlist)

  def limit(self, count):
    if count <= 0:
      return Fc([])
    newlist = []
    c1 = 0
    for it in self.__mylist:
      newlist.append(it)
      if c1 == count - 1:
        break
      else:
        c1 += 1
    return Fc(newlist)

  # ---------- The following cannot be chained ----------

  def reduce(self, func):
    if not isinstance(func, FunctionType):
      raise FcTypeError(str(func) + " is Not Function")
    return reduce(func, self.__mylist)

  def len(self):
    return len(list(self.__mylist))

  def count(self):
    return len(list(self.__mylist))

  def done(self):
    return list(self.__mylist)

  def list(self):
    '''Just an alias for done.'''
    return self.done()

  def iter(self):
    return self.__mylist

  # ---------- Magic Methods ----------

  def __iter__(self):
    return iter(self.iter())
