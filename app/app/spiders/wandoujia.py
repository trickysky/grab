#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/12/21

from app import items
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from base import LOCAL_MONGO as mongo

class Wandoujia(CrawlSpider):
    name = 'wandoujia'
    collection = mongo.local.app_wandoujia
    custom_settings = {
        'ITEM_PIPELINES': {
            'app.pipelines.WandoujiaAppPipeline': 999,
        }
    }
    allowed_domains = [
        'wandoujia.com'
    ]
    start_urls = [
        'http://www.wandoujia.com/apps',
        'http://www.wandoujia.com/category/app',
        'http://www.wandoujia.com/category/game',
        'http://www.wandoujia.com/top/app',
        'http://www.wandoujia.com/essential/app'
        'http://www.wandoujia.com/essential/game'
    ]
    rules = {
        Rule(LinkExtractor(allow=('/apps/[^/]+$',)), callback='parse_detail', follow=True),
        Rule(LinkExtractor(allow=('/category.*'), allow_domains='wandoujia.com')),
        Rule(LinkExtractor(allow=('/tag.*'), allow_domains='wandoujia.com')),
        Rule(LinkExtractor(allow=('/essential.*'), allow_domains='wandoujia.com')),
        Rule(LinkExtractor(allow=('/top.*'), allow_domains='wandoujia.com')),
        Rule(LinkExtractor(allow=('/special.*'), allow_domains='wandoujia.com')),
    }

    def parse_detail(self, response):
        item = items.WandoujiaItem()
        app_info = response.xpath('//div[@class="download-wp"]/a')
        item['app_name'] = ''.join(app_info.xpath('@data-name').extract())
        item['package_name'] = ''.join(app_info.xpath('@data-app-pname').extract())
        item['app_id'] = ''.join(app_info.xpath('@data-app-id').extract())
        item['app_vid'] = ''.join(app_info.xpath('@data-app-vid').extract())
        item['vcode'] = ''.join(app_info.xpath('@data-app-vcode').extract())
        item['vname'] = ''.join(app_info.xpath('@data-app-vname').extract())
        item['icon'] = ''.join(app_info.xpath('@data-app-icon').extract())
        item['category_id'] = ''.join(app_info.xpath('@data-app-categoryid').extract())
        item['install'] = ''.join(app_info.xpath('@data-install').extract())
        item['praise'] = ''.join(response.xpath('//div[@class="num-list"]/span[@class="item love"]/i/text()').extract())
        item['comment_count'] = ''.join(response.xpath('//div[@class="num-list"]/div[@class="comment-area"]/a/i/text()').extract())
        info_list = response.xpath('//dl[@class="infos-list"]')
        item['category'] = '|'.join(info_list.xpath('//dd[@class="tag-box"]/a/text()').extract())
        item['tag'] = '|'.join(info_list.xpath('//div[@class="side-tags clearfix"]/div[@class="tag-box"]/a/text()').re('\S+'))
        item['app_update_dt'] = ''.join(info_list.xpath('//time/text()').extract())
        item['system'] = ''.join(map(lambda x: x.strip(), info_list.xpath('//dd[@class="perms"]/text()').extract()))
        item['permission'] = '|'.join(info_list.xpath('//span[@class="perms"]/text()').extract())
        item['company'] = ''.join(info_list.xpath('//span[@class="dev-sites"]/text()').extract())
        item['desc'] = '|'.join(response.xpath('//div[@class="desc-info"]/div[@class="con"]/text()').extract())
        item['change'] = '|'.join(response.xpath('//div[@class="change-info"]/div[@class="con"]/text()').extract())
        yield item