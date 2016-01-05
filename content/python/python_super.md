Title: Python super()函数研究
Date: 2015-2-19 20:58
Modified: 2015-2-19
Tags: super
Authur: 转载


在《Learn Python The Hard Way》一书中看到super()的用法，在网上查了下，发现还挺有意思。
###1.问题的发现与提出
在Python类的方法（method）中，要调用父类的某个方法，在Python 2.2以前，通常的写法如下代码：

```python
class A:
	def __init__(self):
		print "enter A"
		print "leave A"

class B(A):
	def __init__(self):
		print "enter B"
		A.__init__(self)
		print "leave B"

>>> b = B()
enter B
enter A
leave A
leave B
```

即，使用非绑定的类方法（用类名来引用的方法），并在参数列表中，引入待绑定的对象（self），从而达到调用父类的目的。

这样做的缺点是，当一个子类的父类发生变化时（如类B的父类由A变为C时），必须遍历整个类定义，把所有的通过非绑定的方法的类名全部替换过来，例如代码段:　

```python
class B(C):              # A --> C
	def __init__(self):
		print "enter B"
		c.__init__(self)  # A --> C
		print "leave B"
```
如果代码简单，这样的改动或许还可以接受。但如果代码量庞大，这样的修改可能是灾难性的。

###2. 问题的解决
因此，自Python 2.2开始，Python添加了一个关键字super，来解决这个问题。下面是Python 2.3的官方文档说明：
>  super(type[, object-or-type])
  Return the superclass of type. If the second argument is omitted the super object
  returned is unbound. If the second argument is an object, isinstance(obj, type)
  must be true. If the second argument is a type, issubclass(type2, type) must be
  true. super() only works for new-style classes.
  A typical use for calling a cooperative superclass method is:
   class C(B):
       def meth(self, arg):
           super(C, self).meth(arg)
  New in version 2.2.

从说明来看，可以把类B改写如下代码段：

```python
class A(object): # A must be new-style class
	def __init__(self):
		print "enter A"
		print "leave A"

class B(C): # A --> C
	def __init__(self):
		print "enter B"
		super(B, self).__init__()
		print "leave B"
```
尝试执行上面同样的代码，结果一致，但修改的代码只有一处，把代码的维护量降到最低，是一个不错的用法。因此在我们的开发过程中，super关键字被大量使用，而且一直表现良好。

在我们的印象中，对于super(B, self).__init__()是这样理解的：super(B, self)首先找到B的父类（就是类A），然后把类B的对象self转换为类A的对象（通过某种方式，一直没有考究是什么方式，惭愧），然后“被转换”的类A对象调用自己的__init__函数。考虑到super中只有指明子类的机制，因此，在多继承的类定义中，通常我们保留使用类似代码段1的方法。
有一天某同事设计了一个相对复杂的类体系结构（我们先不要管这个类体系设计得是否合理，仅把这个例子作为一个题目来研究就好），代码如下代码段：

```python
class A(object):
	def __init__(self):
   		print "enter A"
   		print "leave A"

class B(object):
	def __init__(self):
   		print "enter B"
   		print "leave B"

class C(A):
	def __init__(self):
		print "enter C"
		super(C, self).__init__()
		print "leave C"

class D(A):
	def __init__(self):
   		print "enter D"
   		super(D, self).__init__()
   		print "leave D"

class E(B, C):
	def __init__(self):
   		print "enter E"
   		B.__init__(self)
   		C.__init__(self)
   		print "leave E"

class F(E, D):
	def __init__(self):
		print "enter F"
   		E.__init__(self)
   		D.__init__(self)
   		print "leave F"
```
根据运行的结果，类A和类D的初始化函数被重复调用了2次，这并不是我们所期望的结果！我们所期望的结果是最多只有类A的初始化函数被调用2次——其实这是多继承的类体系必须面对的问题。我们把代码段4的类体系画出来，如下图：

```
    object
   |       \
   |        A
   |      / |
   B     C  D
    \   /   |
      E     |
        \   |
          F
```
按我们对super的理解，从图中可以看出，在调用类C的初始化函数时，应该是调用类A的初始化函数，但事实上却调用了类D的初始化函数。好一个诡异的问题！
也就是说，mro中记录了一个类的所有基类的类类型序列。查看mro的记录，发觉包含7个元素，7个类名分别为：
 F E B C D A object
从而说明了为什么在C.__init__中使用super(C, self).__init__()会调用类D的初始化函数了。
我们把代码段改写为：

```python
class A(object):
	def __init__(self):
   		print "enter A"
   		super(A, self).__init__()  # new
   		print "leave A"

class B(object):
	def __init__(self):
   		print "enter B"
   		super(B, self).__init__()  # new
   		print "leave B"

class C(A):
	def __init__(self):
   		print "enter C"
   		super(C, self).__init__()
   		print "leave C"

class D(A):
	def __init__(self):
   		print "enter D"
   		super(D, self).__init__()
   		print "leave D"

class E(B, C):
	def __init__(self):
   		print "enter E"
   		super(E, self).__init__()  # change
   		print "leave E"

class F(E, D):
	def __init__(self):
   		print "enter F"
   		super(F, self).__init__()  # change
   		print "leave F"
```
根据运行结果，F的初始化不仅完成了所有的父类的调用，而且保证了每一个父类的初始化函数只调用一次。
###3. 延续的讨论
我们再重新看上面的类体系图，如果把每一个类看作图的一个节点，每一个从子类到父类的直接继承关系看作一条有向边，那么该体系图将变为一个有向图。不能发现mro的顺序正好是该有向图的一个拓扑排序序列。
从而，我们得到了另一个结果——Python是如何去处理多继承。支持多继承的传统的面向对象程序语言（如C++）是通过虚拟继承的方式去实现多继承中父类的构造函数被多次调用的问题，而Python则通过mro的方式去处理。
但这给我们一个难题：对于提供类体系的编写者来说，他不知道使用者会怎么使用他的类体系，也就是说，不正确的后续类，可能会导致原有类体系的错误，而且这样的错误非常隐蔽的，也难于发现。
###4. 小结
1. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，产生了一个super对象；
2. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
3. super(B, self).func的调用并不是用于调用当前类的父类的func函数；
4. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数只调用一次（如果每个类都使用super）；
5. 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一个父类函数被调用多次。
