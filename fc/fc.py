from functools import reduce, wraps
from collections import Iterable
from types import FunctionType
from itertools import product


class FcTypeError(Exception):
  pass


class FcRangeError(Exception):
  pass


def paramMustBeFunction(testFunction):
  def test(func):
    return isinstance(func, FunctionType)

  @wraps(testFunction)
  def dealFunction(*args, **kwargs):
    l = len(args)
    if l == 1 and not test(args[0]):
      raise FcTypeError(str(args[0]) + " is Not Function")
    elif l == 2 and not test(args[1]):
      raise FcTypeError(str(args[1]) + " is Not Function")
    return testFunction(*args, **kwargs)

  return dealFunction


class Fc:
  '''
  FunctionChain
  '''

  def __init__(self, mylist):
    if not isinstance(mylist, Iterable):
      raise FcTypeError(str(list) + " is Not Iterable")
    # __mylist is val
    self.__mylist = mylist
    self.__max = None
    self.__min = None
    self.__len = None

  @paramMustBeFunction
  def map(self, func):
    return type(self)(map(func, self.__mylist))

  @paramMustBeFunction
  def filter(self, func):
    return type(self)(filter(func, self.__mylist))

  def set(self):
    return type(self)(set(self.__mylist))

  def sort(self, func=None):
    if func is None:
      return type(self)(list(sorted(self.__mylist)))
    else:
      if not isinstance(func, FunctionType):
        raise FcTypeError(str(func) + " is Not Function")
      return type(self)(list(sorted(self.__mylist, key=func)))

  def resort(self, func=None):
    if func is None:
      return type(self)(sorted(self.__mylist, reverse=True))
    else:
      if not isinstance(func, FunctionType):
        raise FcTypeError(str(func) + " is Not Function")
      return type(self)(sorted(self.__mylist, key=func, reverse=True))

  def getAfter(self, start, count=-1):
    def tmp(start, count=-1):
      if start < 0:
        start = 0
      c1 = 0
      c2 = 0
      for it in self.__mylist:
        if c1 >= start:
          if c2 >= count and count != -1:
            break
          else:
            yield it
            c2 += 1
        c1 += 1

    return type(self)(tmp(start, count))

  def skip(self, count):
    # if count <= 0:
    #   return self
    # def tmp(count):
    #   c1 = 0
    #   for it in self.__mylist:
    #     if c1 >= count:
    #       yield it
    #     c1 += 1
    # return type(self)(tmp(count))
    return self.getAfter(count)

  def dropLast(self, count):
    if count < 0:
      raise FcRangeError(str(count) + " can not be less than 0")
    elif count == 0:
      return self
    else:
      l = self.list()
      if len(l) > count:
        l = l[:-count]
      else:
        l = []
      return type(self)(l)

  def slice(self, indexList):
    indexList = sorted(indexList)

    def tmp(indexList):
      i = 0
      ii = 0  # indexList index @_@
      l = len(indexList)
      if l == 0: return
      if indexList[0] < 0:
        raise FcRangeError(str(indexList[0]) + " can not be less than 0")
      for it in self.__mylist:
        if ii >= l:
          return
        else:
          if i == indexList[ii]:
            ii += 1
            yield it
        i += 1

    return type(self)(tmp(indexList))

  def drop(self, count):
    return self.skip(count)

  def limit(self, count):
    if count <= 0:
      return type(self)([])

    def tmp(count):
      c1 = 0
      for it in self.__mylist:
        yield it
        if c1 == count - 1:
          break
        else:
          c1 += 1

    return type(self)(tmp(count))

  def take(self, count):
    return self.limit(count)

  def takeLast(self, count):
    if count < 0:
      raise FcRangeError(str(count) + " can not be less than 0")
    elif count == 0:
      return type(self)([])
    else:
      l = self.list()
      if len(l) > count:
        l = l[len(l) - count:]
      else:
        pass
      return type(self)(l)

  # other is Iterable
  def cat(self, other):
    if not isinstance(other, Iterable):
      raise FcTypeError(str(other) + "is not Iterable")

    def tmp(other):
      for it in self.__mylist:
        yield it
      for it in other:
        yield it

    return type(self)(tmp(other))

  def catTail(self, other):
    return self.cat(other)

  def catHead(self, other):
    if not isinstance(other, Iterable):
      raise FcTypeError(str(other) + "is not Iterable")

    def tmp(other):
      for it in other:
        yield it
      for it in self.__mylist:
        yield it

    return type(self)(tmp(other))

  # other is object
  def add(self, other):
    def tmp(other):
      for it in self.__mylist:
        yield it
      yield other

    return type(self)(tmp(other))

  def append(self, other):
    return self.add(object)

  def addTail(self, other):
    return self.add(other)

  def addHead(self, other):
    def tmp(other):
      yield other
      for it in self.__mylist:
        yield it

    return type(self)(tmp(other))

  def filterNotNone(self):
    return self.filter(lambda x: x != None)

  @paramMustBeFunction
  def filterNot(self, func):
    return self.filter(lambda x: not func(x))

  def reverse(self):
    return type(self)(reversed(self.__mylist))

  def insert(self, index, value):
    if index < 0:
      raise FcRangeError(str(index) + " can not be less than 0")

    def tmp(index):
      i = 0
      for it in self.__mylist:
        if i == index:
          yield value
          yield it
        else:
          yield it
        i += 1

    return type(self)(tmp(index))

  def insertList(self, index, vlist):
    if index < 0:
      raise FcRangeError(str(index) + " can not be less than 0")
    if not isinstance(vlist, Iterable):
      raise FcTypeError(str(vlist) + " is Not Iterable")

    def tmp(index):
      i = 0
      for it in self.__mylist:
        if i == index:
          for lit in vlist:
            yield lit
          yield it
        else:
          yield it
        i += 1

    return type(self)(tmp(index))

  def product(self, *vlist):
    if not isinstance(vlist[0], Iterable):
      raise FcTypeError(str(vlist[0]) + " is Not Iterable")
    return type(self)(product(self.__mylist, *vlist))

  # some iterable like `map`,just can only be consumed once
  def print(self):
    tmp = list(self.__mylist)
    print(tmp)
    return type(self)(tmp)

  def show(self):
    return self.print()

  # ---------- Cannot be chained ----------

  def index(self, index):
    i = 0
    for it in self.__mylist:
      if i == index:
        return it
      i += 1
    return None

  def any(self, obj):
    for it in self.__mylist:
      if it == obj:
        return True
    else:
      return False

  def empty(self):
    for _ in self.__mylist:
      return False
    return True

  def none(self, obj):
    return not self.any(obj)

  def max(self):
    if self.__max != None:
      return self.__max
    else:
      try:
        self.__max = max(self.__mylist)
      except ValueError as e:
        return None
      return self.__max

  def min(self):
    if self.__min != None:
      return self.__min
    else:
      try:
        self.__min = min(self.__mylist)
      except ValueError as e:
        return None
      return self.__min

  def sum(self):
    s = None
    for it in self.__mylist:
      if s == None:
        s = it
      else:
        try:
          s += it
        except TypeError:
          raise FcTypeError(str(it) + " cannot add " + str(s))
    return s

  @paramMustBeFunction
  def sumBy(self, func):
    return self.map(func).sum()

  def all(self, obj):
    for it in self.__mylist:
      if it != obj:
        return False
    else:
      return True

  @paramMustBeFunction
  def reduce(self, func):
    return reduce(func, self.__mylist)

  def len(self):
    if self.__len == None:
      self.__len = len(list(self.__mylist))
    return self.__len

  def count(self):
    return self.len()

  def size(self):
    return self.len()

  def done(self):
    return list(self.__mylist)

  def list(self):
    '''Just an alias for done.'''
    return self.done()

  @paramMustBeFunction
  def forEach(self, func):
    for it in self.__mylist:
      func(it)

  # param `func` is (int index,obj iter_obj)->{}
  # like Kotlin ;-)
  @paramMustBeFunction
  def forEachIndexed(self, func):
    index = 0
    for it in self.__mylist:
      func(index, it)
      index += 1

  @paramMustBeFunction
  def firstOrNone(self, func):
    for it in self.__mylist:
      if func(it) == True: return it
    else:
      return None

  @paramMustBeFunction
  def lastOrNone(self, func):
    saved = None
    for it in self.__mylist:
      if func(it) == True:
        saved = it
    return saved

  @paramMustBeFunction
  def singleOrNone(self, func):
    saved = None
    for it in self.__mylist:
      if func(it) == True:
        if saved == None:
          saved = it
        else:
          return None
    return saved

  def iter(self):
    return self.__mylist

  # ---------- Magic Methods ----------

  def __iter__(self):
    return iter(self.iter())

  def __str__(self):
    return str(self.list())

  def __add__(self, other):
    return self.catTail(other)

  def __radd__(self, other):
    return self.catHead(other)

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type != None:
      print(exc_type)
      print(exc_val)
      print(exc_tb)


newDict = {}
for name in Fc.__dict__:
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  newName = ""
  for c in name:
    if c in upper:
      newName += "_" + c.lower()
    else:
      newName += c
  newDict[newName] = Fc.__dict__[name]
Fc_ = type("Fc_", (object,), newDict)

#
# def funcable(string):
#   return eval(string)


# clean field
del newDict

if __name__ == "__main__":
  pass
