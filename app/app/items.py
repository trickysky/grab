# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduAppItem(scrapy.Item):
    app_id = scrapy.Field()
    keyword  = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    type = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()
    download_num = scrapy.Field()
    description = scrapy.Field()
