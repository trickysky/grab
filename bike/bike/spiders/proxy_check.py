#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/17

from scrapy.spiders import CrawlSpider
from bike.models import *

class ProxyCheck(CrawlSpider):
    name = 'proxy_check'
    db = db
    models = {
        # 'proxy': proxy.spider_proxy,
    }
