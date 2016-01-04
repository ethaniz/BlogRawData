Title: MAC OS X中解决 socket.error:[Errno 48]Address already in use 端口占用问题
Date: 2015-2-17 21:06
Tags: pelican
Slug: pelican_socket
Authur: Ethaniz

###

###问题
在OS X中使用Pelican搭建blog，在`make serve`停止以后，再次`make serve`出现报错端口已被占用。

###原因
由于python导致退出不完整，后台的python进程还是存在，导致端口一直占用不释放。

###解决办法
找到占用端口的进程pid，然后kill

>lsof命令
>一个列出当前系统打开文件的工具。在类UNIX环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接的硬件。

```
sudo lsof -i:8000
```
显示结果

```
COMMAND     PID          USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Google    37757 nightfalldust  204u  IPv4 0xfe9cdf1b4a4f3119      0t0  TCP localhost:57766->localhost:irdmi (SYN_SENT)
Python    78791 nightfalldust    3u  IPv4 0xfe9cdf1b51e5fb89      0t0  TCP *:irdmi (LISTEN)
```
然后使用`sudo kill 78791`解决问题。