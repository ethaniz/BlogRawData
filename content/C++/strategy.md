Title: 策略模式
Date: 2015-1-25 10:28:00
Modified: 2015-1-25
Tags: Design Pattern
Authur: Ethaniz

- **使用场景**： 针对同一接口有许多种不同的算法，每种算法可以用一个子类来实现，同时有一个基类来抽象出共同的部分。比如：商场的各种打折方式，直接打折，满200送30等等。
- 需要有一个strategyContext的类，传入子类对象，客户端通过`new`strategyContext类来调用算法的统一接口。
```
class strategyContext
{
	public:
	AlgorithmBase * m_algorithm;
	strategyContext(AlgorithmBase * base)
	{
		m_algorithm = base;
	};
	void algorithmInterface()
	{
		m_algorithm->algorithmInterface()
	}
}
```
- **优势**： 将具体算法封装，隔离，实现算法的快速替换。客户端`new`出strategyContext类并调用算法接口即可。将算法的变化和算法的使用者隔离。
- **问题**： 客户端仍需了解各种算法子类
- **可能的解决方法**：结合简单工厂模式，修改strategyContext的构造函数，在构造函数中通过传入特征值来`new`不同的strategy子类并赋予m_algorithm。使用strategyContext来依赖各种算法子类，客户端不用知晓具体的算法子类，只用知晓有哪些算法即可。
- **同工厂模式的区别**
	- 工厂模式给出需求，要求工厂返回具体的对象，隔离对象的创建过程
	- 策略模式先创造出具体对象，并通过strategyContext来统一使用对象，隔离对象的变化
