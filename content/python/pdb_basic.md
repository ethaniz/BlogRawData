Title: Pdb basic usage
Date: 2015-3-10 11:59:00
Modified: 2015-3-10
Tags: Pdb
Authur: Ethaniz

####使用方法
1. `python -m pdb xxx.py`
2.
``` python
import pdb
#在需要打断点的地方
pdb.set_trace()
```

####命令

|命令	|  解释 |
| --- | ----|
|break 或 b | 设置断点 |
|continue 或 c|	继续执行程序
|list 或 l|	查看当前行的代码段
|step 或 s|	进入函数
|return 或 r|	执行代码直到从当前函数返回
|exit 或 q|	中止并退出
|next 或 n|	执行下一行
|pp|	打印变量的值
|help|	帮助
