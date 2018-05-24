# Fc v0.1.8 文档

**重要**：如果需要查找特定函数，请使用 `Ctrl+F` 快速查找

## Fc 异常

- FcTypeError：当出现例如构造 Fc 类的参数不是 `Iterable` 类型的情况、或者传递给 `map` 等需要函数参数的函数不是 `FunctionType` 的时候，就会抛出此异常
- FcRangeError：当出现例如传递给 `dropLast` 的参数小于 0 时，则会抛出此异常

## 装饰器

- paramMustBeFunction：检查类成员函数的第二个参数(第一个是 self)是否为 `FunctionType`，不是则抛出异常

## Fc 类

## Magic 方法

函数名|参数|返回值|功能|备注
---|---|---|---|---
`__init__`|可迭代对象|None|初始化，并把这个可迭代对象当做 `val`(不可变，代码软实现)，同时定义各种缓存，避免重复计算|如果参数不是 `Iterable`，则抛出 `FcTypeError`

```Python
f = Fc([1,2,3,4])
f = Fc(range(1,5))
```

---

函数名|参数|返回值|功能|备注
---|---|---|---|---
`__add__`/`__radd__`|None|连接后的新 Fc|重载了 `+` 操作，并可以实现 Fc 与可迭代对象的加法(连接)|该加法不是 `append`，如需添加元素，可以使用 `insert` 插入某个位置或者使用 `add` 或 `append` 加入结尾

```Python
assert (Fc([1,2])+[3,4]).done() == [1, 2, 3, 4]
assert ([1,2]+Fc([3,4])).done() == [1, 2, 3, 4]
assert (Fc([1,2])+Fc([3,4])).done() == [1, 2, 3, 4]
```

---

函数名|参数|返回值|功能|备注
---|---|---|---|---
`__str__`|None|字符串|返回 List 类型的字符串|这里会遍历全部的元素，所以可能会有性能影响

```Python
assert str(Fc([1, 2, 3]))=="[1, 2, 3]"
```

---

函数名|参数|返回值|功能|备注
---|---|---|---|---
`__iter__`|None|可迭代对象|使得 Fc 可以直接加入 for 中|并且没有性能影响

```Python
l = [1, 2]
nl = []
for i in Fc(l):
  nl.append(i)
assert nl == [1, 2]
```

---

函数名|参数|返回值|功能|备注
---|---|---|---|---
`__enter__`/`__exit__`|None|Fc 的 self|为了实现 `with Fc(...) as ...` 的用法|似乎没啥用

```Python
with Fc([1,2,3]) as f:
  f.print()
  # [1, 2, 3]
```

---

## 可链式调用

特点：**返回值都为 Fc**，都提供了 opt 的优化选项，默认为 True，False 仅当需要防止迭代器特性而造成一次性消费的情况使用，例如

```Python
  f = Fc([1, 2]).map(lambda x: x)
  print(f.size(), end="\t")
  f.print()
  # 2	[]

  f = Fc([1, 2]).map(lambda x: x, opt=False)
  print(f.size(), end="\t")
  f.print()
  # 2	[1, 2]
```

优化这个并不代表好坏，通过自己实际情况选择性使用。

函数名|参数|功能|备注
---|---|---|---
`map`|函数|接受一个函数，并用此函数对每个元素进行处理，并将结果集合作为一个新的 Fc 返回|三大板斧之一

```Python
l = [1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).map(lambda x: x + 1).done()
assert ml == [2, 3, 4, 5, 6, 7, 8]
```

---

函数名|参数|功能|备注
---|---|---|---
`count`|None|给 Fc 计数，返回('元素',出现次数)元组的数组，例如[('a',4),('b',5)]|建议配合 sort 等使用

```Python
assert Fc([
  1, 2, 3, 4,
  1, 2, 3, 4,
  1, 2, 3, 4,
  1, 2, 3, 4,
]).count().sort(lambda x: x[0]).done() == [
         (1, 4),
         (2, 4),
         (3, 4),
         (4, 4),
       ]
```

---

函数名|参数|功能|备注
---|---|---|---
`filter`|函数|删除不满足函数条件的元素，并返回剩下元素|三大板斧之一
`filterNot`|函数|删除满足函数条件的元素，并返回剩下元素|filter 的变相实现
`filterNotNone`|None|删除列表里所有的 `None` 元素|filter 便捷操作

```Python
l = [1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).filter(lambda x: x > 3).filter(lambda x: x < 6).done()
assert ml == [4, 5]

l = [1, None, None, None, 7]
ml = Fc(l).filterNot(lambda x: x == None).done()
assert ml == [1, 7]
```

---

函数名|参数|功能|备注
---|---|---|---
`set`|None|将元素去重，并返回一个**无序**集合|通常用于不注重顺序的去重操作

```Python
l = [1, 1, 2, 3, 3]
ml = Fc(l).set()
for i in [1, 2, 3]:
  assert i in ml
assert ml.size() == 3
```

---

函数名|参数|功能|备注
---|---|---|---
`sort`|排序依照函数，为空则按照默认的排序|排序|
`resort`|排序依照函数，为空则按照默认的排序|逆序|
`reverse`|None|倒序|倒序仅仅只是把顺序反过来，不是反向排序

```Python
l = [7, 6, 5, 4, 3, 2, 1]
ml = Fc(l).sort().done()
assert ml == [1, 2, 3, 4, 5, 6, 7]

l = [1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).resort().done()
assert ml == [7, 6, 5, 4, 3, 2, 1]

l = [1, 3, 2, 4]
assert Fc(l).reverse().done() == [4, 2, 3, 1]
```

---

函数名|参数|功能|备注
---|---|---|---
`getAfter`|start:从第几个元素开始，count:取之后的多少个|获取 start 位置之后的 count 个元素|如果 start<0 则以 0 算，如果 count 大于整个长度，则返回 start 之后的所有元素，如果要获取 start 之后的元素，那么只填 start 就好了，count 默认为 -1，即不做数量限制
`skip`/`drop`|跳过数量|跳过 count 个元素，即 `getAfter` 函数的简化版

```Python
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

l = [0, 1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).skip(-1).done()
assert ml == [0, 1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).skip(2).done()
assert ml == [2, 3, 4, 5, 6, 7]
ml = Fc(l).skip(10).done()
assert ml == []

# drop 是 skip 的一个代理作用相同
```

---

函数名|参数|功能|备注
---|---|---|---
`dropLast`|数量|丢弃最后 n 个元素，返回前面的元素|当 count <0 时会抛出 `FcRangeError` 异常，**这个函数未使用生成器实现，所以对性能可能会有影响**

```Python
l = [0, 1, 2, 3, 4, 5, 6, 7]
try:
  Fc(l).dropLast(-1).done()
  assert "FcRangeError not thrown" == "False"
except FcRangeError as e:
  assert 1 == 1
assert Fc(l).dropLast(4).done() == [0, 1, 2, 3]
```

---

函数名|参数|功能|备注
---|---|---|---
`slice`|index 的 list|返回 index 对应的元素列表|当超过范围则会忽略超过部分

```Python
l = [0, 1, 2, 3, 4, 5, 6, 7]
assert Fc(l).slice([1, 5, 6]).done() == [1, 5, 6]
assert Fc(l).slice([1, 5, 6, 10]).done() == [1, 5, 6]
try:
  assert Fc(l).slice([-1, 2, 3]).done() == [2, 3]
  assert "FcRangeError not thrown" == "False"
except FcRangeError as e:
  assert 1 == 1
```

---

函数名|参数|功能|备注
---|---|---|---
`limit`/`take`|数量|取前 n 个元素|当 n <= 0 时，返回 Fc([])

```Python
l = [0, 1, 2, 3, 4, 5, 6, 7]
ml = Fc(l).limit(-1).done()
assert ml == []
ml = Fc(l).limit(0).done()
assert ml == []
ml = Fc(l).limit(3).done()
assert ml == [0, 1, 2]
ml = Fc(l).limit(10).done()
assert ml == l
```

---

函数名|参数|功能|备注
---|---|---|---
takeLast|数量|取最后 n 个元素|**这个函数未使用生成器实现，所以对性能可能会有影响**

```Python
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
```

---

函数名|参数|功能|备注
---|---|---|---
`cat`/`catHead`/`catTail`|可迭代对象|把可迭代对象连接在 Fc 后面/前面|`cat` 等价于 `catTail`
`add`/`append`/`addTail`/`addHead`|普通元素对象|把对象添加到在 Fc 后面/前面|`add` 等价于 `append` 等价于 `addTail`
`insert`|位置，值|在某个位置插入某个元素，如果越界则忽略，小于 0 则抛出 `FcRangeError` 异常
`insertList`|位置，List|在某个位置插入一个列表，如果越界则忽略

```Python
l = [1, 2, 3]
l2 = [4, 5, 6]
assert Fc(l).cat(l2).done() == [1, 2, 3, 4, 5, 6]
assert Fc(l).catTail(l2).done() == [1, 2, 3, 4, 5, 6]
assert Fc(l).catHead(l2).done() == [4, 5, 6, 1, 2, 3]

l = [1, 2, 3]
v = 4
assert Fc(l).add(v).done() == [1, 2, 3, 4]
assert Fc(l).addTail(v).done() == [1, 2, 3, 4]
assert Fc(l).addHead(v).done() == [4, 1, 2, 3]

assert (Fc([1, 2]) + [3, 4]).done() == [1, 2, 3, 4]
assert ([1, 2] + Fc([3, 4])).done() == [1, 2, 3, 4]
assert (Fc([1, 2]) + Fc([3, 4])).done() == [1, 2, 3, 4]

l = [1, 2, 3, 4]
assert Fc(l).insert(0, 0).done() == [0, 1, 2, 3, 4]
assert Fc(l).insert(10, 0).done() == l
try:
  Fc(l).insert(-1, 1).done()
  assert "FcRangeError not thrown" == "False"
except FcRangeError as e:
  assert 1 == 1

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
```

---

函数名|参数|功能|备注
---|---|---|---
`product`|列表|求笛卡尔积，并以 Fc((a,b)) 的形式返回|要注意的是，返回元素不是原来的结构，而是以元组的形式返回；可以传递多个列表进行求笛卡尔积

```Python
l = [1, 2]
l2 = [3, 4]
assert Fc(l).product(l2).done() == [
  (1, 3),
  (1, 4),
  (2, 3),
  (2, 4),
]
```

---

函数名|参数|功能|备注
---|---|---|---
`print`/`show`|None|以 List 的方式打印 Fc|可以链式调用，**这个函数未使用生成器实现，所以对性能可能会有影响**，顺便记录以下这里的一个坑，当 `map` 之类的函数被迭代一次之后，原来的对象就会清除，所以要提前把 `map` 出来的数据缓存起来

```Python
Fc([1,2,3]).print().show()
# [1, 2, 3]
# [1, 2, 3]
```

## 不可链式调用

特点：**返回值不为 Fc**，这里要注意的是，因为 Fc 是采用的迭代器优化策略，所以由于迭代器的一次性消费特性，下列函数每次使用都会改变 Fc 的状态，所以如果需要保存 Fc，则最好在上一个 Fc 对象上关闭 opt，即设置 opt = False

函数名|参数|返回值|功能|备注
---|---|---|---|---
`reduce`|处理函数|处理后的值|对元素进行叠加处理|三板斧之一
`index`|下标|元素|返回对应位置的元素|使用了迭代计数，所以性能上影响不大，越界返回 None
`any`|元素|布尔|检测元素是否存在，存在返回 True，否则 False|
`all`|元素|布尔|检测 Fc 里是否全为参数元素，是则返回 True，否则 False|
`none`|元素|布尔|和 `any` 相反，不存在则返回 True，否则 False|
`empty`|None|布尔|检测 Fc 是否为空|
`max`|None|元素|返回最大值，为空则返回 None|会缓存
`min`|None|元素|返回最小值，为空则返回 None|会缓存
`sum`|None|值|对 Fc 求和|类型无法相加则会返回 `FcTypeError`
`sumBy`|函数|值|先根据函数处理，再求和|异常抛出情况如 `sum`
`len`/`size`|None|值|求 Fc 的长度|这两个等价
`done`/`list`|None|列表|把 Fc 从迭代器转换成 list|方便 print 或者切片操作
`forEach`|函数|None|用参数函数对每个元素进行处理，例如 print 等等|函数类型为单参数(元素)
`forEachIndexed`|函数|None|用参数函数对每个元素进行处理，例如 print 等等|函数类型为双参数(index,元素)
`firstOrNone`|函数|对象|返回满足函数条件的第一个值，当未找到的时候，返回 None|自己实现的，所以会不用担心性能问题
`lastOrNone`|函数|对象|返回满足函数条件的最后一个值，当未找到的时候，返回 None|**这个函数对性能可能会有影响**，原因是复杂度为 O(n)
`singleOrNone`|函数|对象|当满足条件的元素唯一，则返回对象，否则返回 None|**这个函数对性能可能会有影响**，原因是复杂度为 O(n)
`iter`|None|可迭代对象|直接返回可迭代对象

## 关于此文档

- 2018-05-24 更新 v0.1.8(改得不多，海星)
- 2018-05-23 更新 v0.1.7(写到头晕)
- 2018-05-22 更新 v0.1.3(写到头疼)