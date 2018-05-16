from functools import reduce


class Fc:
  '''
  FunctionChain
  '''

  def __init__(self, mylist):
    self.list = mylist

  def map(self, func):
    return Fc(list(map(func, self.list)))

  def filter(self, func):
    return Fc(list(filter(func, self.list)))

  def sorted(self, func):
    return Fc(list(sorted(self.list, key=func)))

  def reduce(self, func):
    return Fc(list(reduce(func, self.list)))

  def len(self):
    return len(self.list)

  def done(self):
    return self.list


if __name__ == "__main__":
  l = [1, 2, 3, 4, 5, 6, 7]
  print(Fc(l).map(lambda x: x + 1).done())
  print(Fc(l).filter(lambda x: x > 3).done())
  print(Fc(l).filter(lambda x: x > 3).filter(lambda x: x < 6).done())
  print(Fc(l).filter(lambda x: x > 5).len())

