#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/12

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ProxyFetch(CrawlSpider):
    name = 'proxy_fetch'
    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'spiderman.middlewares.ProxyMiddleware': 301,
    #     }
    # }

    # start_urls = ['http://www.xicidaili.com/nn']
    # rules = (
    #     Rule(LinkExtractor(allow=('nn\/\d+',)), callback='parse_proxy'),
    # )
    #
    # def parse_proxy(self, response):
    #     print response.url

    def start_requests(self):
        yield scrapy.http.Request(url='http://www.xicidaili.com/nn', callback=self.parse)

    def parse(self, response):
        print response.status
        print response.body
