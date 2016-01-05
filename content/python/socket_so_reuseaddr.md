Title: Socket SO_REUSEADDR
Date: 2015-4-22 15:51:00
Modified: 2015-4-22
Tags: Socket
Authur: Ethaniz

####背景
最近用Python写个UDP server程序，偶然发现如果server由于crush等异常退出，再继续运行脚本会出现一直卡在`bind()`函数的状态。

研究了下，发现是因为crush之前的server socket绑定了某个port，然后异常退出导致这个port的资源没有释放，重启之后需要继续在该port上绑定会出现绑不上的情况。

####解决
在申请socket之后，给socket设置以下参数：
```python
self.send_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
```

####度娘解释`SO_REUSEADDR`
>设置套接字选项为SO_REUSEADDR，socket可重用，经常在socket通信时进行设置。
>
>编写 TCP/SOCK_STREAM 服务程序时，SO_REUSEADDR到底什么意思？

>这个套接字选项通知内核，如果端口忙，但TCP状态位于 TIME_WAIT ，可以重用端口。如果端口忙，而TCP状态位于其他状态，重用端口时依旧得到一个错误信息，指明"地址已经使用中"。如果你的服务程序停止后想立即重启，而新套接字依旧使用同一端口，此时 SO_REUSEADDR 选项非常有用。必须意识到，此时任何非期望数据到达，都可能导致服务程序反应混乱，不过这只是一种可能，事实上很不可能。

>一个套接字由相关五元组构成，协议、本地地址、本地端口、远程地址、远程端口。SO_REUSEADDR 仅仅表示可以重用本地本地地址、本地端口，整个相关五元组还是唯一确定的。所以，重启后的服务程序有可能收到非期望数据。必须慎重使用 SO_REUSEADDR 选项。
