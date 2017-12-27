# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduAppItem(scrapy.Item):
    app_id = scrapy.Field()
    # keyword  = scrapy.Field()
    type = scrapy.Field()
    subtype = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    tag = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()
    download_num = scrapy.Field()
    description = scrapy.Field()
    package = scrapy.Field()
    download_link = scrapy.Field()


class WandoujiaItem(scrapy.Item):
    app_name = scrapy.Field()
    package_name = scrapy.Field()
    app_id = scrapy.Field()
    app_vid = scrapy.Field()
    vcode = scrapy.Field()
    vname = scrapy.Field()
    icon = scrapy.Field()
    category_id = scrapy.Field()
    install = scrapy.Field()
    praise = scrapy.Field()
    comment_count = scrapy.Field()
    category = scrapy.Field()
    tag = scrapy.Field()
    app_update_dt = scrapy.Field()
    system = scrapy.Field()
    permission = scrapy.Field()
    company = scrapy.Field()
    desc = scrapy.Field()
    change = scrapy.Field()