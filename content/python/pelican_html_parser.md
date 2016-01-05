Title: Error of Pelican on Mac - No module named html_parser
Date: 2015-2-17 22:03
Modified: 2015-2-17
Tags: Pelican
Authur: Ethaniz


> 安裝 **Pelican** 時出現以下錯誤：**No module named html_parser**

這是因為 Mac 自帶的 six module 是 1.4.1 版，所以會發生這個問題，即使用 pip 安裝 six 最新版，仍然無法蓋過去。

檢查方式如下：
在 Python 的環境下輸入下列指令檢查版本：

```python
import six
printf six.__version__
```
解決方法：
不要用 pip 安裝，直接到 six 的官網：https://pypi.python.org/pypi/six/ 下載 source，解壓縮後用下列指令安裝：

```
sudo python setup.py install
```
