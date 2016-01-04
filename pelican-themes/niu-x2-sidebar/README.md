# Niu-X2-Sidebar

Niu-X2-Sidebar is a responsive theme for pelican, built with bootstrap3.

As I am pretty new to bootstrap and jinja2, the codes look messy and may be buggy. If you find any bugs, please let me know.

## License

BSD 3-Clause License. Please see LICENSE.txt for more details.

## Demo

![Demo image of niu-x2 theme](https://raw.github.com/mawenbao/niu-x2-sidebar/master/screenshot.png "niu-x2-sidebar demo image")

You can check my blog [blog.atime.me](http://blog.atime.me) for a live demo.

Other demos:

1. [J-Cn.me](http://J-Cn.me)

## Features
*  Responsive.
*  Disqus, duoshuo, google analytics and google custom search support.
*  Pagination bar with customizable length. 
*  Tagcloud implemented with [tagcloud.js](https://code.google.com/p/tagcloud) which supports incremental search.
*  Collapsible monthly archives.
*  Auto-generated copyright year range, which is actually from the year of your first article to the lastest.
*  Fixed position navigation bar.
*  TOC(table of contents) in sidebar with the help of [extract_headings](https://github.com/wilbur-ma/extract_headings) plugin, with no addtional dependencies and no `[TOC]` in your markdown file.
*  Article/Page comment on/off controled by file metadata.
*  Pygments theme support.
*  Categories shown in a dropdown list.
*  Category aliases, which should be useful when you set `USE_FOLDER_AS_CATEGORY` to `True`.
*  Custom dropdown menu, footer links and footer icons through pelican configuration with custom icons.
*  Translations through pelican configuration.
*  Lazy load images with the jquery.lazy.load plugin. (You have to manually set `NIUX2_LAZY_LOAD` as True)
*  A toolbar.
*  Support for hermit audio player.

## Usage

If you are hosting your pelican site locally, please remeber to set the `SITEURL` variable empty in your pelican configuration, otherwise the theme will not be able to find the css and js static files correctly. 

For more theme related configurations, please refer to `Theme settings` section below.

First clone the repository:

    git clone https://github.com/mawenbao/niu-x2-sidebar

Then set `THEME` variable to the path of the repository folder you have just cloned in your pelican configuration.

    THEME = ~/repo/niu-x2-sidebar

The theme depends on the jinja2 `expression statement` extension which should be added to your pelican configuration as below:

    JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]

## TODO

1. Better responsive support.

## Global pelican settings

Currently the following pelican configuration variables are supported:

*  `DISQUS_SITENAME` is your disqus site ID.
*  `GOOGLE_ANALYTICS` is your Google analytics ID.

## SEO
Currently this theme supports keywords meta tag and description meta tag. The content of keywords meta tag is set as the value of `Tags` metadata. And the content of description meta tag is set as the value of `Desc` metadata.

## Theme settings

Note that:

*  All the following theme configuration variables are optional.
*  All the icons are selected from [iconmoon](https://icomoon.io)(most of them are from font-awesome). You can select your own icons from [here](https://icomoon.io/app/) and replace the default icons at `static/font-icons`.

### Custom home name

* `NIUX2_HOME_NAME`, defalut SITENAME.  

### Enable/Disable comments

The theme enables comments for all the articles and pages by default. However you can disable comments for some particular articles or pages by setting `Comment` metadata to any value other than `on`, e.g.:

    Title: An Article With No Comments
    Date: 2013-09-09 21:38:00
    Comment: off

### TOC style
The following configuration will hide the sidebar TOC.

    Title: An Article With No TOC
    Date: 2013-09-09 21:38:00
    TOC: closed

And the following configuration will make TOC fixed, which is the default behaviour when TOC is not configured:

    Title: An Article With fixed TOC
    Date: 2013-09-09 21:38:00
    TOC: fixed

Any values other than 'closed' and 'fixed' will make TOC's position static.

### Debug niu2.js
`niu2.js` is the main script used in this theme. By default the theme uses the minified version `niu2.min.js` which can be generated by the given Makefile. If you want to use `niu2.js` instead of `niu2.min.js`, just set `NIUX2_DEBUG` as `True` in your pelican configuration file.

### Archives order by update date
This function requires the [pelican-update-date](https://github.com/mawenbao/pelican-update-date) plugin.

You should add the following setting to your pelican configuration.

    TEMPLATE_PAGES = {
        "archives_updatedate.html": "archives_updatedate.html",
    }

### Article Navigation
[Neighbors](https://github.com/getpelican/pelican-plugins/tree/f7174a25b47675ed8429f432ef3a682c55c2fcf1/neighbors) is needed.  
Using *_article_in_category by default.

### Lazy load images
This function requires the [niux2_lazyload_helper](https://github.com/mawenbao/niux2_lazyload_helper) plugin.

Lazy load images(with the class name `lazy`) in the main content area with the lazyload jquery plugin.

* `NIUX2_LAZY_LOAD`, default(False): enable lazy load function.
* `NIUX2_LAZY_LOAD_TEXT`, default('Loading'): the hover text upon images when loading.
* `NIUX2_LAZY_LOAD_ICON`, default('icon-spin icon-spinner'): class of the icon upon images when loading.

### hermit audio player
This function requires the [niux2_hermit_player](https://github.com/mawenbao/niux2_hermit_player) plugin.

### Custom 404

*  `NIUX2_404_TITLE_TRANSL` string(default "ERROR 404 Page Not Found!"), title of the 404 page
*  `NIUX2_404_INFO_TRANSL` string(default "The requested url was not found!"), warning infomation on the 404 page

You should add the following setting to your pelican configuration.

    TEMPLATE_PAGES = {
        "404.html": "404.html",
    }

### Toolbar

The toolbar only supports for github/bitbucket project now.

*  `NIUX2_TOOLBAR` bool(default False), enable/disable toolbar.
*  `NIUX2_GITHUB_REPO` string(default ''), repository of your github project, for example `mawenbao/niu-x2-sidebar`.
*  `NIUX2_BITBUCKET_REPO` string(default ''), repository of your bitbucket project, for example `mawenbao/niu-x2-sidebar`. Note that this setting will be ignored if `NIUX2_GITHUB_REPO` has been set.

### Pygments theme

First make sure you have enabled the `codehilite` markdown extension(pelican enables it by default). Then you can pick you favorite theme
in the `static/css/pygments` folder. Currently all the theme css files come from the [pygments-css](https://github.com/richleland/pygments-css) repository. At last you should set the `NIUX2_PYGMENTS_THEME` variable to the file name of the theme with no .css extension at the end. For example:

    NIUX2_PYGMENTS_THEME = 'borland'

If `NIUX2_PYGMENTS_THEME` is not set, niu-x2-sidebar uses `github` theme by default.

### Google custom search engine

*  `NIUX2_GOOGLE_CSE_ID` is your your google custom [search engine id](http://support.google.com/customsearch/bin/answer.py?hl=en&answer=2649143).
*  `NIUX2_SEARCH_TRANSL` is the search text displayed in header bar, which is "Search" by default.
*  `NIUX2_SEARCH_PLACEHOLDER_TRANSL` is the placeholder of your search box, which is "Press enter to search ..." by default. 

The css codes above will set the width of your search box to 200px.

#### Limitations

Currently, there is not a search result page in this theme, so I suggest that you display the search results in a Google-hosted page. 

### Category aliases

`NIUX2_CATEGORY_MAP` is a dictionary of category aliases, of which each item follows the format `original name: (display name, icon class)`, if you do not want a icon, just leave the icon class empty. e.g.:

    NIUX2_CATEGORY_MAP = {
        "code": ("代码", "icon-code")
        "note": ("笔记", ""),
    }

### Navigation bar

`NIUX2_HEADER_SECTIONS` is a list of links displayed on the fixed position navigation bar. Each link element is a tuple with the format `(link value, link title, link href, icon class)` e.g.:

    NIUX2_HEADER_SECTIONS = [ 
         ("关于", "about", "/about.html", "icon-anchor"),
         ("存档", "archives", "/archives.html", "icon-archive"),
         ("标签", "tags", "/tag/", "icon-tag"),
    ]

`NIUX2_HEADER_DROPDOWN_SECTIONS` is a dictionary of dropdown menu. The key is a tuple with the format `(display name, icon class)`, and the corresponding value is actually a `NIUX2_HEADER_SECTIONS` list, e.g.:

    NIUX2_HEADER_DROPDOWN_SECTIONS = [
        ("custom drop down", "icon-archive"): [
            ("关于", "about", "/about.html", "icon-anchor"),
            ("存档", "archives", "/archives.html", "icon-archive"),
            ],
        ("custom drop down2", "icon-folder-open"): [
            ("标签", "tags", "/tag/", "icon-tag"),
            ],
    ]

### Apple touch icons
Example configuraton:

    # sizes => href
    NIUX2_APPLE_ICON_MAP = { 
        '': '/apple-touch-icon-57x57.png'
        '76x76': '/apple-touch-icon-76x76.png',
        '120x120': '/apple-touch-icon-120x120.png',
        '152x152': '/apple-touch-icon-152x152.png',
    }
    NIUX2_APPLE_PRECOMPOSED_ICON_MAP = {
        '': '/apple-touch-icon-precomposed-57x57.png'
        '76x76': '/apple-touch-icon-precomposed-76x76.png',
        '120x120': '/apple-touch-icon-precomposed-120x120.png',
        '152x152': '/apple-touch-icon-precomposed-152x152.png',
    }

    EXTRA_PATH_METADATA = {
        'extra/apple-touch-icon-76x76.png': { 'path': 'apple-touch-icon-76x76.png' },
        'extra/apple-touch-icon-120x120.png': { 'path': 'apple-touch-icon-120x120.png' },
        'extra/apple-touch-icon-152x152.png': { 'path': 'apple-touch-icon-152x152.png' },
    }

And then drop your apple touch icons into the `content/extra` directory.

### Footer icons

`NIUX2_FOOTER_ICONS` is a list of icon links shown in the footer section. Each element follows the format `(icon class, link title, link href)`, e.g.:

    NIUX2_FOOTER_ICONS = [
         ("icon-envelope-alt", "my email address", "mailto: wilbur.ma@foxmail.com"),
         ("icon-github-alt", "my github page", "http://github.com/wilbur-ma"),
         ("icon-rss", "subscribe my blog via rss", "http://atime.me/feed.xml"),
         ]

### Translation settings

*  `NIUX2_404_TITLE_TRANSL` string(default "ERROR 404 Page Not Found!"), title of the 404 page
*  `NIUX2_404_INFO_TRANSL` string(default "The requested url was not found!"), warning infomation on the 404 page
*  `NIUX2_TAG_TRANSL` string(default "Tag"), translation of tag
*  `NIUX2_ARCHIVE_TRANSL` string(default "Archives"), translation of archives
*  `NIUX2_ARCHIVE_UPDATEDATE_TRANSL` string(default "Archives(by updatedate)"), translation of archives by update date
*  `NIUX2_CATEGORY_TRANSL` string(default "Category"), translation of category
*  `NIUX2_TAG_CLEAR_TRANSL` string(default "clear"), name of clear button on the tags page
*  `NIUX2_TAG_FILTER_TRANSL` string(default "filter tags"), placeholder of the tag_filter input on the tags page
*  `NIUX2_HEADER_TOC_TRANSL` string(default "TOC"), name of the categories dropdown menu
*  `NIUX2_SEARCH_TRANSL` string(default "Search"), name displayed for google cse in the header bar
*  `NIUX2_SEARCH_PLACEHOLDER_TRANSL` string(default "Press enter to search ..."), placeholder of the header search box
*  `NIUX2_COMMENTS_TRANSL` string(default "Comments"), translation of comments
*  `NIUX2_PUBLISHED_TRANSL` string(default "Published"), translation of publish date
*  `NIUX2_LASTMOD_TRANSL` string(default "Last modified"), translation of last modified label, need pelican update_date plugin support
*  `NIUX2_RECENT_UPDATE_TRANSL` string(default "Recent Updated Posts"), translation of recent updated posts
*  `NIUX2_HIDE_SIDEBAR_TRANSL` string(default "Hide Sidebar")
*  `NIUX2_SHOW_SIDEBAR_TRANSL` string(default "Show Sidebar")
*  `NIUX2_REVISION_HISTORY_TRANSL` string(default "Revision History")
*  `NIUX2_VIEW_SOURCE_TRANSL` string(default "View Source")
*  `NIUX2_AUTHOR_TRANSL` string(default "Author")

### Misc settings

*  `NIUX2_BAIDU_TJ` string(default ""), baidu tongji id.
*  `NIUX2_TOOLBAR_LOAD_ICON` string(default "icon-spin icon-4x icon-spinner"), the class of the rotating icon which shows on top the whole page when we hide/show sidebar toc.
*  `NIUX2_PAGINATOR_LENGTH` int(default 11), the length of your pagination bar
*  `NIUX2_FAVICON_URL` string(default "/favicon.png"), your favicon url
*  `NIUX2_FOOTER_LINKS` a `NIUX2_HEADER_SECTIONS` format list shown right after your copyright info in the footer section
*  `NIUX2_DISPLAY_TITLE` boolean(default True), whether to display the title of article and page
*  `NIUX2_DUOSHUO_SHORTNAME` string(default None), your duoshuo shortname. Note that if `DISQUS_SITENAME` is set, duoshuo will not be loaded.
*  `NIUX2_DUOSHUO_THREAD_KEY` string(default ""), type of your duoshuo thread key. If you want to use article's slug for its thread key, change it to 'slug' or 'date' for using article's date. Otherwise, it will use part of the article's url as its thread key by default.
*  `NIUX2_LIB_THEME` string(default SITEURL+'/theme'), url of niu-x2-sidebar theme root
*  `NIUX2_LIB_FONT_ICONS` string(default SITEURL+'/theme/font-icons'), url of your custom font icons.
*  `NIUX2_LIB_FONTAWESOME` string(default ''), url of font awesome icons.
*  `NIUX2_LIB_BOOTSTRAP` string(default SITEURL+'/theme'), url of bootstrap library
*  `NIUX2_LIB_JQUERY` string(default SITEURL+'/theme/js/jquery-1.10.2.min.js'), url of jquery
*  `NIUX2_LAZY_LOAD` bool(default False), enable lazy loading images.
*  `NIUX2_DEBUG` bool(default False), if set as True, use niu2.js instead of niu2.min.js
*  `NIUX2_AUTHOR_LINK` string(default 'SITEURL'), the author link of ariticles
*  `NIUX2_RECENT_UPDATE_NUM` int(default 10), number of your recent updated posts in the sidebar, require [pelican-update-date](https://github.com/mawenbao/pelican-update-date) plugin
