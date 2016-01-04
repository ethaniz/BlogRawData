Title: 如何在C++中调用C程序
Date: 2015-6-3 15:18:00
Modified: 2015-6-3
Tags: c++
Authur: Ethaniz

C＋＋和C是两种完全不同的编译链接处理方式，如果直接在C＋＋里面调用C函数，会找不到函数体，报链接错误。要解决这个问题，就要在 C＋＋文件里面显示声明一下哪些函数是C写的，要用C的方式来处理。

>1.引用头文件前需要加上 extern “C”，如果引用多个，那么就如下所示
```
extern “C”
{
#include “ s.h”
#include “t.h”
#include “g.h”
#include “j.h”
};
```
然后在调用这些函数之前，需要将函数也全部声明一遍。
>2.C++调用C函数的方法,将用到的函数全部重新声明一遍
```
extern “C”
{
extern void A_app（int）;
extern void B_app（int）;
extern void C_app（int）;
extern void D_app（int）;
}
```

####C++程序中调用被c编译器编译后的函数，为什么要加extern "C"？
C++语言支持函数重载，C语言不支持函数重载。函数被C++编译后在库中的名字与C语言的不同。假设某个C 函数的声明如下：
```
void foo(int x, int y);
```
该函数被C 编译器编译后在库中的名字为_foo，而C++编译器则会产生像_foo_int_int之类的名字用来支持函数重载和类型安全连接。由于编译后的名字不同，C++程序不能直接调用C 函数。C++提供了一个C 连接交换指定符号extern“C”来解决这个问题。例如：
```
extern “C”
{
void foo(int x, int y);
// 其它函数
}
```
或者写成
```
extern “C”
{
#include “myheader.h”
// 其它C 头文件
}
```
这就告诉C++编译译器，函数 foo 是个C 连接，应该到库中找名字_foo 而不是找_foo_int_int。C++编译器开发商已经对C 标准库的头文件作了extern“C”处理，所以我们可以用#include 直接引用这些头文件。