#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ethaniz'
SITENAME = u'异尘余生'
SITEURL = u'http://ethaniz.github.io'

#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES = True

PATH = 'content'

TIMEZONE = u'Asia/Shanghai'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

THEME = './pelican-themes/niu-x2-sidebar'
JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]

USE_FOLDER_AS_CATEGORY = True

# using Bootswatch Yeti
# BS3_THEME = 'http://bootswatch.com/yeti/bootstrap.min.css'

#PYGMENTS_STYLE = 'colorful'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = False

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'http://github.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

BOOTSTRAP_THEME = 'yeti'
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_TAGS_INLINE = True

DISPLAY_CATEGORIES_ON_MENU = True

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

DISQUS_SITENAME = 'ethaniz'
DISQUS_ID_PREFIX_SLUG = True

GITHUB_USER = 'Ethaniz'
GITHUB_REPO_COUNT = 5

# niu-x2 theme config
NIUX2_AUTHOR_TRANSL = '作者'
NIUX2_404_TITLE_TRANSL = '404错误 页面未找到!'
NIUX2_404_INFO_TRANSL = '请求页面未找到!'
NIUX2_TAG_TRANSL = '标签'
NIUX2_ARCHIVE_TRANSL = '存档'
NIUX2_ARCHIVE_UPDATEDATE_TRANSL = '存档 (按修改时间)'
NIUX2_CATEGORY_TRANSL = '分类'
NIUX2_TAG_CLEAR_TRANSL = '清空'
NIUX2_TAG_FILTER_TRANSL = '过滤标签'
NIUX2_HEADER_TOC_TRANSL = '目录'
NIUX2_SEARCH_TRANSL = '搜索'
NIUX2_SEARCH_PLACEHOLDER_TRANSL = '按回车开始搜索 ...'
NIUX2_COMMENTS_TRANSL = '评论'
NIUX2_PUBLISHED_TRANSL = '发布时间'
NIUX2_LASTMOD_TRANSL = '最后修改'
NIUX2_PAGE_TITLE_TRANSL = '页面'
NIUX2_RECENT_UPDATE_TRANSL = '最近修改'
NIUX2_HIDE_SIDEBAR_TRANSL = '隐藏侧边栏'
NIUX2_SHOW_SIDEBAR_TRANSL = '显示侧边栏'
NIUX2_REVISION_HISTORY_TRANSL = '修订历史'
NIUX2_VIEW_SOURCE_TRANSL = '查看源文件'

NIUX2_PYGMENTS_THEME = 'github'
NIUX2_PAGINATOR_LENGTH = 11
NIUX2_RECENT_UPDATE_NUM = 10
#NIUX2_FAVICON_URL = '/favicon.ico'
#NIUX2_GOOGLE_CSE_ID = '016368690064160370938:8u3wwjza9c4'
NIUX2_DISPLAY_TITLE = True
#NIUX2_LAZY_LOAD = True
#NIUX2_LAZY_LOAD_TEXT = 'orz 努力加载中'
NIUX2_TOOLBAR = True
#NIUX2_GITHUB_REPO = 'mawenbao/pelican-blog-content'

NIUX2_CATEGORY_MAP = {
    'code': ('代码', 'fa-code'),
    'collection': ('搜藏', 'fa-briefcase'),
    'essay': ('随笔', 'fa-leaf'),
    'life': ('日常', 'fa-coffee'),
    'note': ('笔记', 'fa-book'),
    'research': ('研究', 'fa-flask'),
}

NIUX2_HEADER_SECTIONS = [
    ('关于', 'about me', '/about.html', 'fa-anchor'),
    ('项目', 'my projects', '/my_projects.html', 'fa-rocket'),
    #('标签', 'tags', '/tags/', 'fa-tag'),
    ('标签', 'tags', '/tags.html', 'fa-tag'),
]

#NIUX2_HEADER_DROPDOWN_SECTIONS = OrderedDict()
#NIUX2_HEADER_DROPDOWN_SECTIONS[('存档', 'fa-archive')] = [
#    ('存档 (按发布时间)', 'archives order by publish time', '/archives.html', 'fa-calendar'),
#    ('存档 (按修改时间)', 'archives order by modify time', '/archives_updatedate.html', 'fa-pencil'),
#]

NIUX2_FOOTER_LINKS = [
    ('关于', 'about me', '/about.html', ''),
]

NIUX2_FOOTER_ICONS = [
    ('fa-key', 'my public key', '/my_gnupg.html'),
    ('fa-envelope-o', 'my email address', 'mailto: mawenbao@hotmail.com'),
    ('fa-github-alt', 'my github page', 'http://github.com/mawenbao'),
    ('fa-rss', 'subscribe my blog', '/feed.xml'),
]