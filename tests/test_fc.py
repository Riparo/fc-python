from fc import Fc
from fc import FcTypeError
from fc import FcRangeError

'''
Use `Pytest` as a test framework
'''


def test_map():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).map(lambda x: x + 1).done() == [2, 3, 4, 5, 6, 7, 8]


def test_product():
  assert Fc([1, 2]).product([3, 4]).done() == [
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
  ]


def test_filter():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).filter(lambda x: x > 3).filter(lambda x: x < 6).done() == [4, 5]


def test_set():
  for i in [1, 2, 3]:
    assert i in Fc([1, 1, 2, 3, 3]).set()
  assert Fc([1, 1, 2, 3, 3]).set().size() == 3


def test_insert():
  assert Fc([1, 2, 3, 4]).insert(0, 0).done() == [0, 1, 2, 3, 4]
  assert Fc([1, 2, 3, 4]).insert(10, 0).done() == [1, 2, 3, 4]
  try:
    Fc([1, 2, 3, 4]).insert(-1, 1).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1


def test_insertList():
  assert Fc([2, 3, 4]).insertList(0, [0, 1]).done() == [0, 1, 2, 3, 4]
  assert Fc([2, 3, 4]).insertList(10, [0, 1, 2, 3]).done() == [2, 3, 4]
  try:
    Fc([2, 3, 4]).insertList(-1, [0]).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1
  try:
    Fc([2, 3, 4]).insertList(1, 0).done()
    assert "FcTypeError not thrown" == "False"
  except FcTypeError as e:
    assert 1 == 1


def test_sort():
  assert Fc([7, 6, 5, 4, 3, 2, 1]).sort().done() == [1, 2, 3, 4, 5, 6, 7]


def test_resort():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).resort().done() == [7, 6, 5, 4, 3, 2, 1]


def test_getAfter():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).getAfter(-20).done() == [0, 1, 2, 3, 4, 5, 6, 7]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).getAfter(2).done() == [2, 3, 4, 5, 6, 7]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).getAfter(4, 1).done() == [4]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).getAfter(0, 2).done() == [0, 1]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).getAfter(4, 0).done() == []


def test_skip_drop():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).skip(-1).done() == [0, 1, 2, 3, 4, 5, 6, 7]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).skip(2).done() == [2, 3, 4, 5, 6, 7]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).skip(10).done() == []


def test_dropLast():
  try:
    Fc([0, 1, 2, 3, 4, 5, 6, 7]).dropLast(-1).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).dropLast(4).done() == [0, 1, 2, 3]


def test_slice():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).slice([1, 5, 6]).done() == [1, 5, 6]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).slice([1, 5, 6, 10]).done() == [1, 5, 6]
  try:
    assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).slice([-1, 2, 3]).done() == [2, 3]
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1


def test_limit_take():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).limit(-1).done() == []
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).limit(0).done() == []
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).limit(3).done() == [0, 1, 2]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).limit(10).done() == [0, 1, 2, 3, 4, 5, 6, 7]


def test_add_addTail_addHead_append():
  assert Fc([1, 2, 3]).add(4).done() == [1, 2, 3, 4]
  assert Fc([1, 2, 3]).addTail(4).done() == [1, 2, 3, 4]
  assert Fc([1, 2, 3]).addHead(4).done() == [4, 1, 2, 3]

  assert (Fc([1, 2]) + [3, 4]).done() == [1, 2, 3, 4]
  assert ([1, 2] + Fc([3, 4])).done() == [1, 2, 3, 4]
  assert (Fc([1, 2]) + Fc([3, 4])).done() == [1, 2, 3, 4]


def test_cat_catTail_catHead():
  assert Fc([1, 2, 3]).cat([4, 5, 6]).done() == [1, 2, 3, 4, 5, 6]
  assert Fc([1, 2, 3]).catTail([4, 5, 6]).done() == [1, 2, 3, 4, 5, 6]
  assert Fc([1, 2, 3]).catHead([4, 5, 6]).done() == [4, 5, 6, 1, 2, 3]


def test_string():
  assert str(Fc([1, 2, 3])) == "[1, 2, 3]"


def test_taskLast():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).takeLast(10).done() == [0, 1, 2, 3, 4, 5, 6, 7]
  try:
    Fc([0, 1, 2, 3, 4, 5, 6, 7]).takeLast(-1).done()
    assert "FcRangeError not thrown" == "False"
  except FcRangeError as e:
    assert 1 == 1
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).takeLast(3).done() == [5, 6, 7]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).takeLast(8).done() == [0, 1, 2, 3, 4, 5, 6, 7]
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).takeLast(0).done() == []


def test_len():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).filter(lambda x: x < 1).len() == 0
  assert Fc([1, 2, 3, 4, 5, 6, 7]).filter(lambda x: x > 4).len() == 3
  assert Fc([1, 2, 3, 4, 5, 6, 7]).filter(lambda x: x > 1 and x < 6).len() == 4


def test_reduce():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).reduce(lambda x, y: x + y) == 28


def test_forEach():
  ml = []
  Fc([0, 1, 2, 3, 4, 5, 6, 7]).forEach(lambda x: ml.append(x))
  assert ml == [0, 1, 2, 3, 4, 5, 6, 7]


def test_forEachIndexed():
  ml = []
  Fc([0, 1, 2]).forEachIndexed(lambda i, x: ml.append((i, x)))
  assert ml == [
    (0, 0),
    (1, 1),
    (2, 2),
  ]


def test_firstOrNone():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).firstOrNone(lambda x: x == 10) == None
  assert Fc([1, 2, 3, 4, 5, 6, 7]).firstOrNone(lambda x: x >= 3) == 3


def test_lastOrNull():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).lastOrNone(lambda x: x == 10) == None
  assert Fc([1, 2, 3, 4, 5, 6, 7]).lastOrNone(lambda x: x >= 3) == 7


def test_singleOrNull():
  assert Fc([1, 2, 3, 4, 5, 6, 7]).singleOrNone(lambda x: x == 10) == None
  assert Fc([1, 2, 3, 4, 5, 6, 7]).singleOrNone(lambda x: x >= 3) == None
  assert Fc([1, 2, 3, 4, 5, 6, 7]).singleOrNone(lambda x: x == 3) == 3


def test_filterNotNull():
  assert Fc([1, None, None, None, 7]).filterNotNone().done() == [1, 7]


def test_filterNot():
  assert Fc([1, None, None, None, 7]).filterNot(lambda x: x == None).done() == [1, 7]


def test_index():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).index(3) == 3
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).index(30) == None


def test_any():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).any(3) == True
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).any(10) == False


def test_empty():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).empty() == False
  assert Fc([]).empty() == True


def test_joinBy():
  assert Fc([1, 2, 3]).joinBy(",") == "1,2,3"
  assert Fc([]).joinBy(",") == ""
  assert Fc([1]).joinBy(",") == "1"
  assert Fc([1, 2]).joinBy(",") == "1,2"


def test_none():
  assert Fc([0, 1, 2, 3, 4, 5, 6, 7]).none(10)
  assert not Fc([0, 1, 2, 3, 4, 5, 6, 7]).none(1)


def test_all():
  assert Fc([1, 1, 1, 1, 1, 1, 1]).all(1) == True
  assert Fc([1, 1, 1, 1, 1, 1, 1]).all(2) == False
  assert Fc([1, 1, 2, 1, 1, 1, 1]).all(1) == False
  assert Fc([1, 1, 2, 1, 1, 1, 1]).all(2) == False


def test_max_and_min():
  assert Fc([]).max() == None
  assert Fc([]).min() == None
  assert Fc([1, 2]).max() == 2
  assert Fc([1, 2]).min() == 1


def test_sumBy():
  assert Fc([{"a": 1}, {"a": 2}]).sumBy(lambda x: x["a"]) == 3


def test_reversed():
  assert Fc([1, 3, 2, 4]).reverse().done() == [4, 2, 3, 1]


def test_sum():
  assert Fc([]).sum() == None
  assert Fc([1, 2, 3, 4]).sum() == 10
  try:
    Fc([1, 2, 3, None]).sum()
    assert "FcTypeError not thrown" == "False"
  except FcTypeError as e:
    assert 1 == 1


def test_iter():
  nl = []
  for i in Fc([1, 2, 3, 4, 5, 6, 7]).filter(lambda x: x > 2 and x < 5).iter():
    nl.append(i)
  assert nl == [3, 4]


def test_magic_iter():
  nl = []
  for i in Fc([1, 2, 3, 4, 5, 6, 7]).filter(lambda x: x > 2 and x < 5):
    nl.append(i)
  assert nl == [3, 4]


def test_magic_add():
  assert (Fc([1]) + Fc([2])).done() == [1, 2]
  assert (Fc([1]) + [2]).done() == [1, 2]
  assert (Fc([2]) + Fc([1])).done() == [2, 1]
  assert (Fc([2]) + [1]).done() == [2, 1]
