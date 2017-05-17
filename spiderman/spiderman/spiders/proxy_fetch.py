#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/12

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spiderman.items import ProxyItem
from spiderman.model.base import PG_DB as db
from spiderman.model import proxy


class ProxyFetch(CrawlSpider):
    name = 'proxy_fetch'
    db = db
    models = {
        'proxy': proxy.spider_proxy,
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'spiderman.pipelines.ProxyPipeline': 999,
        },
        'DOWNLOAD_DELAY': 1,
    }

    start_urls = [
        'http://www.xicidaili.com/nn',
        'http://www.xicidaili.com/nt',
        'http://www.xicidaili.com/wn',
        'http://www.xicidaili.com/wt',
    ]

    rules = (
        Rule(LinkExtractor(allow=('nn\/\d+',)), follow=True, callback='parse_detail'),
        Rule(LinkExtractor(allow=('nt\/\d+',)), follow=True, callback='parse_detail'),
        Rule(LinkExtractor(allow=('wn\/\d+',)), follow=True, callback='parse_detail'),
        Rule(LinkExtractor(allow=('wt\/\d+',)), follow=True, callback='parse_detail'),
    )

    def parse_detail(self, response):
        page_proxy_trs = response.xpath('//table[@id="ip_list"]/tr[position()>1]')
        for i in page_proxy_trs:
            host = i.xpath('./td[2]/text()').extract_first()
            port = i.xpath('./td[3]/text()').extract_first()
            proxy_type = i.xpath('./td[6]/text()').extract_first()
            item = ProxyItem()
            item['host'] = host
            item['port'] = port
            item['type'] = proxy_type.lower()
            yield item
