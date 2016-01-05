Title: 如何判断一个对象是可迭代
Date: 2015-3-8 11:50:00
Modified: 2015-3-8
Tags: Iterable
Authur: Ethaniz

可迭代对象的好处，可以使用`for ... in`循环。

如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
``` python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```
