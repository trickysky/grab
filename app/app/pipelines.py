# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from base import BasePipeline
import re

class BaiduAppPipeline(BasePipeline):
    def process_item(self, item, spider):
        model_baidu = spider.models['baidu']
        check_query = model_baidu.select().where(model_baidu.app_id == item['app_id'])
        if check_query.exists():
            keyword = model_baidu.get(app_id=item['app_id']).keyword
            if not re.compile(item['keyword']).search(keyword):
                model_baidu.update(keyword='%s,%s' % (keyword, item['keyword'])).where(app_id=item['app_id'])
        else:
            model_baidu.create(
                app_id=item['app_id'],
                keyword=item['keyword'],
                name=item['name'],
                score=item['score'],
                type=item['type'],
                size=item['size'],
                version=item['version'],
                download_num=item['download_num'],
                description=item['description']
            )
        return item
