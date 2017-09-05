# -*- coding: utf-8 -*-
import scrapy
from app import items
from app.models import *
from urllib import quote
import re, time

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    db = db
    # allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']
    models = {
        'baidu': spide_app_baidu
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'app.pipelines.BaiduAppPipeline': 999,
        }
    }

    def start_requests(self):
        keyword = u'购物app'
        page = 68
        for i in range(1, page+1):
            url = 'http://shouji.baidu.com/s?data_type=app&multi=0&ajax=1&wd=%s&page=%s&_=%s' % (quote(keyword.encode('utf-8')), i, int(time.time()*1000))
            yield scrapy.http.Request(url=url, meta={'keyword': keyword}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        keyword = response.meta['keyword']
        if response.body:
            for href in response.xpath('//a[@class="app-name"]/@href').extract():
                url = 'http://shouji.baidu.com%s' % href
                yield scrapy.http.Request(url=url, meta={'keyword': keyword}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = items.BaiduAppItem()
        item['keyword'] = response.meta['keyword']
        item['app_id'] = "".join(re.findall('/(\d+).html$', response.url))
        item['name'] = "".join(response.xpath('//div[@class="yui3-g"]//h1[@class="app-name"]/span/text()').re('\S+'))
        item['score'] = "".join(response.xpath('//div[@class="yui3-g"]//span[@class="star-percent"]/@style').re('\d+'))
        item['type'] = ",".join(response.xpath('//div[@class="yui3-g"]//span[@class="app-feature-detail"]/span/text()').re('\S+'))
        item['size'] = "".join(response.xpath('//div[@class="yui3-g"]//div[@class="detail"]/span[@class="size"]/text()').re(': (\S+)$'))
        item['version'] = "".join(response.xpath('//div[@class="yui3-g"]//div[@class="detail"]/span[@class="version"]/text()').re(': (\S+)$'))
        item['download_num'] = "".join(response.xpath('//div[@class="yui3-g"]//div[@class="detail"]/span[@class="download-num"]/text()').re(': (\S+)$'))
        item['description'] = "".join(response.xpath('//div[@class="brief-long"]/p/text()').re('\S+'))
        print 'app_id %s' % item['app_id'], item['name'], response.url
        yield item
