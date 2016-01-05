Title: 使用Pelican和Github Pages搭建个人博客
Date: 2015-2-19 10:38:00
Modified: 2015-2-19
Tags: pelican
Authur: Ethaniz

####安装pelican和markdown
```
pip install pelican
pip install markdown
```
####主体搭建
```
mkdir blog
cd blog
pelican-quickstart
```
配置项都可默认，以后也可在`pelicanconf.py`中更改。
####命令成功后，出现pelican的框架
```
blog/
├── content                # 存放输入的markdown或RST源文件
│   └── (pages)            # 存放手工创建的静态页面，可选
├── output                 # 存放最终生成的静态博客
├── develop_server.sh      # 测试服务器
├── Makefile               # 管理博客的Makefile
├── pelicanconf.py         # 配置文件
└── publishconf.py         # 发布文件，可删除
```
####书写博文
创建`.md`文件于`content`文件夹中，以下内容必需
```
Title: 文章标题
Date: 创建日期
Modified: 修改日期
Category: 文章分类，标志本文处于该分类下
Tags: 文章标签，标志本文处于该标签下
Slug: URL中该文章的链接地址
Author: 作者
```
写完后，回到blog目录，执行`pelican content`进行博客的生成，存放于`output`文件夹
接着进入`output`文件夹执行`python -m pelican.server`开启测试服务器.在浏览器中输入`http://localhost:8000`即可看到效果
####博文发布
进入`output`目录，执行
```
git init
git add .
git remote add origin https://github.com/xxx/xxx.github.io
git pull origin master
git commit -m 'first blog'
git push origin master
```
####增加新的博文
在`content`目录增加新的`.md`文件，并`make html`，然后在`output`目录
```
git add .
git commit -m 'xxx'
git push origin master
```
####更改主题
主题位于`blog/pelican-theme/`文件夹中，进入改文件夹，选好theme（或者`git clone`新的主题到这个文件夹中），修改`pelicanconf.py`中`THEME = './pelican-themes/xxx'`

####日期格式修改
`DEFAULT_DATE_FORMAT = ('%Y-%m-%d')`

####增加第三方评论系统disqus
https://disqus.com/admin/signup中注册，并且修改`pelicanconf.py`中`DISQUS_SITENAME = 'ethaniz'`
