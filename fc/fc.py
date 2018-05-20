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

  def limit(self, start, count=-1):
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