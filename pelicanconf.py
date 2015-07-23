#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"su'o jbopre"
SITENAME = u'banski'
SITEMOTTO = u'a venue for Lojban enthusiasts'
SITEURL = 'http://banski.github.io'
PLUGINS = ['tag_cloud', ]
THEME = 'bootstrap'
CUSTOM_CSS = 'theme/css/custom.css'
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = tuple()

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_STEPS = 3
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
DEFAULT_PAGINATION = 10

CC_LICENSE = 'by'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISQUS_SITENAME = "banski"
