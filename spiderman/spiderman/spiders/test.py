#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import scrapy


class Test(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        yield scrapy.http.Request(url='http://ip.cip.cc', callback=self.parse)

    def parse(self, response):
        print response.body.strip()