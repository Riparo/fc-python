from fc import Fc
from fc import FcTypeError
from fc import FcRangeError

'''
Use `Pytest` as a test framework
'''


def test_map():
  l = [1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).map(lambda x: x + 1).done()
  assert ml == [2, 3, 4, 5, 6, 7, 8]


def test_product():
  l = [1, 2]
  l2 = [3, 4]
  assert Fc(l).product(l2).done() == [
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
  ]


def test_filter():
  l = [1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).filter(lambda x: x > 3).filter(lambda x: x < 6).done()
  assert ml == [4, 5]


def test_set():
  l = [1, 1, 2, 3, 3]
  ml = Fc(l).set()
  for i in [1, 2, 3]:
    assert i in ml
  assert ml.size() == 3


def test_insert():
  l = [1, 2, 3, 4]
  assert Fc(l).insert(0, 0).done() == [0, 1, 2, 3, 4]
  assert Fc(l).insert(10, 0).done() == l
  try:
    Fc(l).insert(-1, 1).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1


def test_insertList():
  l = [2, 3, 4]
  assert Fc(l).insertList(0, [0, 1]).done() == [0, 1, 2, 3, 4]
  assert Fc(l).insertList(10, [0, 1, 2, 3]).done() == l
  try:
    Fc(l).insertList(-1, [0]).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1
  try:
    Fc(l).insertList(1, 0).done()
    assert "FcTypeError not thrown" == "False"
  except FcTypeError as e:
    assert 1 == 1


def test_sort():
  l = [7, 6, 5, 4, 3, 2, 1]
  ml = Fc(l).sort().done()
  assert ml == [1, 2, 3, 4, 5, 6, 7]


def test_resort():
  l = [1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).resort().done()
  assert ml == [7, 6, 5, 4, 3, 2, 1]


def test_getAfter():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).getAfter(-20).done()
  assert ml == [0, 1, 2, 3, 4, 5, 6, 7]
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).getAfter(2).done()
  assert ml == [2, 3, 4, 5, 6, 7]
  ml = Fc(l).getAfter(4, 1).done()
  assert ml == [4]
  ml = Fc(l).getAfter(0, 2).done()
  assert ml == [0, 1]
  ml = Fc(l).getAfter(4, 0).done()
  assert ml == []


def test_skip_drop():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).skip(-1).done()
  assert ml == [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).skip(2).done()
  assert ml == [2, 3, 4, 5, 6, 7]
  ml = Fc(l).skip(10).done()
  assert ml == []


def test_dropLast():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  try:
    Fc(l).dropLast(-1).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1
  assert Fc(l).dropLast(4).done() == [0, 1, 2, 3]


def test_slice():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  assert Fc(l).slice([1, 5, 6]).done() == [1, 5, 6]
  assert Fc(l).slice([1, 5, 6, 10]).done() == [1, 5, 6]
  try:
    assert Fc(l).slice([-1, 2, 3]).done() == [2, 3]
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1


def test_limit_take():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).limit(-1).done()
  assert ml == []
  ml = Fc(l).limit(0).done()
  assert ml == []
  ml = Fc(l).limit(3).done()
  assert ml == [0, 1, 2]
  ml = Fc(l).limit(10).done()
  assert ml == l


def test_add_addTail_addHead():
  l = [1, 2, 3]
  v = 4
  assert Fc(l).add(v).done() == [1, 2, 3, 4]
  assert Fc(l).addTail(v).done() == [1, 2, 3, 4]
  assert Fc(l).addHead(v).done() == [4, 1, 2, 3]


def test_cat_catTail_catHead():
  l = [1, 2, 3]
  l2 = [4, 5, 6]
  assert Fc(l).cat(l2).done() == [1, 2, 3, 4, 5, 6]
  assert Fc(l).catTail(l2).done() == [1, 2, 3, 4, 5, 6]
  assert Fc(l).catHead(l2).done() == [4, 5, 6, 1, 2, 3]


def test_taskLast():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).takeLast(10).done()
  assert ml == l
  try:
    Fc(l).takeLast(-1).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1
  ml = Fc(l).takeLast(3).done()
  assert ml == [5, 6, 7]
  ml = Fc(l).takeLast(8).done()
  assert ml == [0, 1, 2, 3, 4, 5, 6, 7]
  ml = Fc(l).takeLast(0).done()
  assert ml == []


def test_len():
  l = [1, 2, 3, 4, 5, 6, 7]
  mll = Fc(l).filter(lambda x: x < 1).len()
  assert mll == 0

  mll = Fc(l).filter(lambda x: x > 4).len()
  assert mll == 3

  mll = Fc(l).filter(lambda x: x > 1 and x < 6).len()
  assert mll == 4


def test_reduce():
  l = [1, 2, 3, 4, 5, 6, 7]
  result = Fc(l).reduce(lambda x, y: x + y)
  assert result == 28


def test_forEach():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  ml = []
  Fc(l).forEach(lambda x: ml.append(x))
  assert ml == [0, 1, 2, 3, 4, 5, 6, 7]


def test_forEachIndexed():
  l = [0, 1, 2]
  ml = []
  Fc(l).forEachIndexed(lambda i, x: ml.append((i, x)))
  assert ml == [
    (0, 0),
    (1, 1),
    (2, 2),
  ]


def test_firstOrNone():
  l = [1, 2, 3, 4, 5, 6, 7]
  mv = Fc(l).firstOrNone(lambda x: x == 10)
  assert mv == None
  mv = Fc(l).firstOrNone(lambda x: x >= 3)
  assert mv == 3


def test_lastOrNull():
  l = [1, 2, 3, 4, 5, 6, 7]
  mv = Fc(l).lastOrNull(lambda x: x == 10)
  assert mv == None
  mv = Fc(l).lastOrNull(lambda x: x >= 3)
  assert mv == 7


def test_singleOrNull():
  l = [1, 2, 3, 4, 5, 6, 7]
  mv = Fc(l).singleOrNull(lambda x: x == 10)
  assert mv == None
  mv = Fc(l).singleOrNull(lambda x: x >= 3)
  assert mv == None
  mv = Fc(l).singleOrNull(lambda x: x == 3)
  assert mv == 3


def test_filterNotNull():
  l = [1, None, None, None, 7]
  ml = Fc(l).filterNotNull().done()
  assert ml == [1, 7]


def test_filterNot():
  l = [1, None, None, None, 7]
  ml = Fc(l).filterNot(lambda x: x == None).done()
  assert ml == [1, 7]


def test_index():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  mv = Fc(l).index(3)
  assert mv == 3


def test_any():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  mv = Fc(l).any(3)
  assert mv == True
  mv = Fc(l).any(10)
  assert mv == False


def test_empty():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  assert Fc(l).empty() == False
  l = []
  assert Fc(l).empty() == True


def test_none():
  l = [0, 1, 2, 3, 4, 5, 6, 7]
  assert Fc(l).none(10)
  assert not Fc(l).none(1)


def test_all():
  l = [1, 1, 1, 1, 1, 1, 1]
  mv = Fc(l).all(1)
  assert mv == True
  mv = Fc(l).all(2)
  assert mv == False
  l = [1, 1, 2, 1, 1, 1, 1]
  mv = Fc(l).all(1)
  assert mv == False
  mv = Fc(l).all(2)
  assert mv == False


def test_max_and_min():
  l = []
  assert Fc(l).max() == None
  assert Fc(l).min() == None
  l = [1, 2]
  assert Fc(l).max() == 2
  assert Fc(l).min() == 1


def test_sumBy():
  l = [{"a": 1}, {"a": 2}]
  assert Fc(l).sumBy(lambda x: x["a"]) == 3


def test_reversed():
  l = [1, 3, 2, 4]
  assert Fc(l).reverse().done() == [4, 2, 3, 1]


def test_sum():
  l = []
  assert Fc(l).sum() == None
  l = [1, 2, 3, 4]
  assert Fc(l).sum() == 10
  l = [1, 2, 3, None]
  try:
    Fc(l).sum()
    assert "FcTypeError not thrown" == "False"
  except FcTypeError as e:
    assert 1 == 1


def test_iter():
  l = [1, 2, 3, 4, 5, 6, 7]
  nl = []
  for i in Fc(l).filter(lambda x: x > 2 and x < 5).iter():
    nl.append(i)
  assert nl == [3, 4]


def test_magic_iter():
  l = [1, 2, 3, 4, 5, 6, 7]
  nl = []
  for i in Fc(l).filter(lambda x: x > 2 and x < 5):
    nl.append(i)
  assert nl == [3, 4]


def test_magic_add():
  l1 = [1]
  l2 = [2]
  assert (Fc(l1) + Fc(l2)).done() == [1, 2]
  assert (Fc(l1) + l2).done() == [1, 2]
  assert (Fc(l2) + Fc(l1)).done() == [2, 1]
  assert (Fc(l2) + l1).done() == [2, 1]
