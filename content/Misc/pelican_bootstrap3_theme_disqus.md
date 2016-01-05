Title: Pelican上使用bootstrap3 theme后无法使用disqus的问题
Date: 2015-2-20 11:38:00
Modified: 2015-2-20
Tags: pelican
Authur: Ethaniz

最近在折腾github上的个人blog，选了好多theme都不尽人意。选来选去还是选择了bootstrap3。但是发现一个致命的问题：Disqus无法工作，显示 “We were unable to load Disqus.”

研究了一下，打开了生成的HTML源文件，搜索 disqus关键字，发现如下代码：
```
var disqus_url = '/pelican_socket.html';
```
问题原来是pelican使用了相对路径，导致disqus的url出错。
于是，配置`pelicanconf.py`如下：
```
SITEURL = u'http://ethaniz.github.io/'
RELATIVE_URLS = False
```
继续测试，观察生成的HTML文件：
```
var disqus_url = 'http://ethaniz.github.io/pelican_html_parser.html';
```
问题宣告解决:)
