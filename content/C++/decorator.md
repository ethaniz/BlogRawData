Title: 装饰模式
Date: 2015-1-29 13:37:00
Modified: 2015-1-29
Tags: Design Pattern
Authur: Ethaniz

- UML图如下
 ![Alt text](http://7xpst3.com1.z0.glb.clouddn.com/DecoratorUML.jpg)
- Component类为被装饰对象的基类
- Decorator类为装饰抽象类，用外类来扩展Component类的功能，而Component类无需知道Decorator的存在
- 代码参考

```
class Decorator:public Component
{
	public:
	Component * m_component;
	Decorator(Component * cp);
	virtual void show()
	{
		m_component->show();
	};
};

class DecoratorA:public Decorator
{
	public:
	virtual void show()
	{
		m_component->show();
		privateOperation();
	};
};

in main()
{
	Component * pInstance = new Component();
	DecoratorA * pDA = new DecoratorA(pInstance);
	DecoratorB * pDB = new DecoratorB(pDA);

	pDB->show();
}
```
