Title: subprocess相关心得
Date: 2015-4-16 11:48:00
Modified: 2015-4-16
Tags: Subprocess
Authur: Ethaniz

最近在项目中，需要写一个在持续集成系统中自动化运行回归测试用例的脚本。思路是使用`subprocess`模块，依次开新进程来运行测试用例，并将用例本身的log输出重定向进文件。
```python
command = 'python Win32Driver.py' + suiteName + testVector
p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

while True:
	buff = p.stdout.readline()
	if p.poll() != None:
		break
		fp.write(buff)
```
这种实现方式本身没有问题，但是仔细推敲，可能存在race condition：子进程不断向管道中输出，而父进程又不断从管道中读取。于是将代码修改如下：
```python
(stdoutdata, stderrdata) = p.communicate()
fp.write(stdoutdata)
```
`p.communicate()`会一直阻塞直到子进程运行完毕，然后一次性将输出写入到文件。
但是这种方式仍然可以会有问题，如果cmd命令输出（标准或错误）过多，PIPE塞满无法继续向PIPE里写入数据，导致死锁。
为解决这个问题，可使用文件来代替PIPE，解除PIPE大小的限制：
```python
p = subprocess.Popen(command, shell=True, stdout = fp, stderr = subprocess.STDOUT)
```
使用这种方法，可以避免使用`communicate()`和`readline()`阻塞，因为一旦子进程hang住的话，父进程也会由于阻塞而完全hang住。
这样，可以在父进程中不断关注子进程的返回值来判断子进程的状态，一旦超时可立即发现:
```python
t = 0
while(t <= 20):
	time.sleep(0.5)
	p.poll()
	if p.returncode != None:
		break
	t+=1
```
