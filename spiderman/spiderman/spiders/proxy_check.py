#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/17

from scrapy.spiders import CrawlSpider
from spiderman.model.base import PG_DB as db
from spiderman.model import proxy


class ProxyCheck(CrawlSpider):
    name = 'proxy_check'
    db = db
    models = {
        'proxy': proxy.spider_proxy,
    }
