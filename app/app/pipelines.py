# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from base import BasePipeline, DEFAULT_REDIS as r
import datetime

class BaiduAppPipeline(BasePipeline):
    def process_item(self, item, spider):
        model_baidu = spider.models['baidu']
        # # check_query = model_baidu.select().where(model_baidu.app_id == item['app_id'])
        # # if check_query.exists():
        # #     keyword = model_baidu.get(app_id=item['app_id']).keyword
        # #     if not item['keyword'] in keyword.split(u','):
        # #         new_keyword = '%s,%s' % (keyword, item['keyword'])
        # #         model_baidu.update(keyword=new_keyword).where(model_baidu.app_id == item['app_id']).execute()
        # else:
        r_key = 'app_%s' % item['app_id']
        if not r.exists(r_key):
            model_baidu.insert(
                app_id=item['app_id'],
                # keyword=item['keyword'],
                type=item['type'],
                subtype=item['subtype'],
                name=item['name'],
                score=item['score'],
                tag=item['tag'],
                size=item['size'],
                version=item['version'],
                download_num=item['download_num'],
                description=item['description'],
            ).execute()
            print 'insert %s %s' % (item['app_id'], item['name'])
        else:
            model_baidu.update(
                type=item['type'],
                subtype=item['subtype'],
                name=item['name'],
                score=item['score'],
                tag=item['tag'],
                size=item['size'],
                version=item['version'],
                download_num=item['download_num'],
                description=item['description'],
            ).where(model_baidu.app_id  == item['app_id']).execute()
            print 'update %s %s' % (item['app_id'], item['name'])
        r.set(r_key, '')
        return item
