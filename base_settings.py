#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/31

LOG_LEVEL = 'INFO'

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'base.CommonRequestMiddleware': 800,
   # 'base.middlewares.ProxyMiddleware': 801,
}

SPIDER_MIDDLEWARES = {
   'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': None,
}
