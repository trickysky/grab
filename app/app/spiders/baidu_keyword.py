# -*- coding: utf-8 -*-
import scrapy
from app import items
from app.models import *
from urllib import quote
import re, time
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BaiduKeyWordSpider(scrapy.Spider):
    name = 'baidu_keyword'
    db = db
    allowed_domains = [
        'baidu.com',
    ]
    models = {
        'baidu': spide_app_baidu
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'app.pipelines.BaiduAppPipeline': 999,
        }
    }

    def start_requests(self):
        keyword_list = {
            u'手术',
        }
        for keyword in keyword_list:
            url = 'http://shouji.baidu.com/s?wd=%s&data_type=app&from=web_alad_5' % quote(keyword.encode('utf-8'))
            yield scrapy.http.Request(url=url, meta={'keyword': keyword, 'page': 0}, callback=self.parse,
                                      dont_filter=True)

    def parse(self, response):
        keyword = response.meta['keyword']
        page = response.meta['page']
        if response.body:
            for href in response.xpath('//a[@class="app-name"]/@href').extract():
                url = 'http://shouji.baidu.com%s' % href
                yield scrapy.http.Request(url=url, meta={'keyword': keyword, 'page': page}, callback=self.parse_detail)
            if 0 == page:
                total_page = int("".join(response.xpath('//input[@class="total-page"]/@value').re('\S+')))
                for page in range(1, total_page + 1):
                    url = 'http://shouji.baidu.com/s?data_type=app&multi=0&ajax=1&wd=%s&page=%s&_=%s' % (
                        quote(keyword.encode('utf-8')), page, int(time.time() * 1000))
                    yield scrapy.http.Request(url=url, meta={'keyword': keyword, 'page': page}, callback=self.parse,
                                              dont_filter=True)

    def parse_detail(self, response):
        keyword = response.meta['keyword']
        page = response.meta['page']
        item = items.BaiduAppItem()
        # item['keyword'] = response.meta['keyword']
        item['type'] = "".join(response.xpath('//div[@class="app-nav"]/div[@class="nav"]/span[3]/a/text()').re('\S+'))
        item['subtype'] = "".join(
            response.xpath('//div[@class="app-nav"]/div[@class="nav"]/span[5]/a/text()').re('\S+'))
        item['app_id'] = "".join(re.findall('/(\d+).html$', response.url))
        item['name'] = "".join(response.xpath('//div[@class="yui3-g"]//h1[@class="app-name"]/span/text()').re('\S+'))
        item['score'] = "".join(response.xpath('//div[@class="yui3-g"]//span[@class="star-percent"]/@style').re('\d+'))
        item['tag'] = ",".join(
            response.xpath('//div[@class="yui3-g"]//span[@class="app-feature-detail"]/span/text()').re('\S+'))
        item['size'] = "".join(
            response.xpath('//div[@class="yui3-g"]//div[@class="detail"]/span[@class="size"]/text()').re(': (\S+)$'))
        item['version'] = "".join(
            response.xpath('//div[@class="yui3-g"]//div[@class="detail"]/span[@class="version"]/text()').re(': (\S+)$'))
        item['download_num'] = "".join(
            response.xpath('//div[@class="yui3-g"]//div[@class="detail"]/span[@class="download-num"]/text()').re(
                ': (\S+)$'))
        item['description'] = "".join(response.xpath('//div[@class="brief-long"]/p/text()').re('\S+'))
        # print keyword, page, item['name'], item['app_id']
        yield item
