Title: 简单工厂模式
Date: 2015-1-23 16:50:00
Modified: 2015-1-23
Tags: Design Pattern
Authur: Ethaniz

- 适合于许多个对象，实现不同的算法，由统一的工厂对象来`new`这些对象

- 优势：利用C++的继承与多态来将不同的算法解耦和，后期维护或者添加新的算法不会对以前的算法造成影响

- 场景举例
	- 计算器实现加、减、乘、除操作
	- 计算不同快递公司的邮费
	- 根据burstType来创建不同的burst，不用关心具体的`new`操作

> **要点**：静态的创造函数

- 举例
```
#include "base.h"

class factory
{
	public:
	static base * create(int op);
}
```
- 客户端调用
```
base * pA = factory::create(1);
base * pB = factory::create(2);
```
