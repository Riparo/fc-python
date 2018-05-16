from functools import reduce


class Fc:
  '''
  FunctionChain
  '''

  def __init__(self, mylist):
    self.__mylist = mylist

  def map(self, func):
    return Fc(map(func, self.__mylist))

  def filter(self, func):
    return Fc(filter(func, self.__mylist))

  def sort(self, func=None):
    if func is None:
      return Fc(list(sorted(self.__mylist)))
    else:
      return Fc(list(sorted(self.__mylist, key=func)))

  def resort(self, func=None):
    if func is None:
      return Fc(sorted(self.__mylist, reverse=True))
    else:
      return Fc(sorted(self.__mylist, key=func, reverse=True))

  # ---------- The following cannot be chained ----------

  def reduce(self, func):
    return reduce(func, self.__mylist)

  def len(self):
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
