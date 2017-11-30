# -*- coding: utf-8 -*-
import scrapy
from app import items
from app.models import *
from urllib import quote
import re, time
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BaiduSpider(CrawlSpider):
    name = 'baidu'
    db = db
    allowed_domains = [
        'baidu.com',
    ]
    start_urls = [
        'http://shouji.baidu.com/',
        'http://shouji.baidu.com/game',
        'http://shouji.baidu.com/software',
        'http://shouji.baidu.com/discovery/top',
        'http://shouji.baidu.com/discovery/pop',
        'http://shouji.baidu.com/discovery/hot',
        'http://shouji.baidu.com/discovery/new',
        'http://shouji.baidu.com/rank/top',
        'http://shouji.baidu.com/rank/up',
        'http://shouji.baidu.com/rank/features',
    ]
    rules = {
        Rule(LinkExtractor(allow=('/game/\d+\.html',)), callback='parse_detail', follow=True),
        Rule(LinkExtractor(allow=('/software/\d+\.html',)), callback='parse_detail', follow=True),
        Rule(LinkExtractor(allow=('/.*'), allow_domains='shouji.baidu.com')),
    }

    models = {
        'baidu': spide_app_baidu
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'app.pipelines.BaiduAppPipeline': 999,
        }
    }

    def parse_detail(self, response):
        item = items.BaiduAppItem()
        item['type'] = "".join(response.xpath('//div[@class="app-nav"]/div[@class="nav"]/span[3]/a/text()').re('\S+'))
        item['subtype'] = "".join(response.xpath('//div[@class="app-nav"]/div[@class="nav"]/span[5]/a/text()').re('\S+'))
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
        item['package'] = "".join(response.xpath('//div[@class="yui3-g"]//div[@class="area-one-setup"]/span[@class="one-setup-btn"]/@data_package').re('\S+'))
        item['download_link'] = "".join(response.xpath('//div[@class="yui3-g"]//div[@class="area-one-setup"]/span[@class="one-setup-btn"]/@data_url').re('\S+'))
        yield item
