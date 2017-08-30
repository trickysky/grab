#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import scrapy
from scrapy.spiders import CrawlSpider

URL = 'http://ip.cip.cc'
# URL = 'http://www.xicidaili.com/nn'


class Test(CrawlSpider):
    name = 'test'
    allowed_domains = ['tiankun.me', 'example.com']
    custom_settings = {

    }
    start_urls = [
        'http://ip.cip.cc'
    ]

    # def start_requests(self):
    #     yield scrapy.http.Request(url=URL, callback=self.parse)

    def parse(self, response):
        print response.body.strip()
