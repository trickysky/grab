#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/31

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'base.CommonRequestMiddleware': 800,
   # 'bike.middlewares.ProxyMiddleware': 801,
}

SPIDER_MIDDLEWARES = {
   'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': None,
}
