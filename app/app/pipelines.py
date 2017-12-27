# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from base import BasePipeline, DEFAULT_REDIS as r, LOCAL_MONGO as mongo
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
        r_key = 'app_baidu_%s' % item['app_id']
        if not r.exists(r_key) or not r.get(r_key) == item['version']:
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
                package=item['package'],
                download_link=item['download_link'],
                create_time=datetime.datetime.now()
            ).execute()
            print 'insert %s %s' % (item['app_id'], item['name'])
        r.set(r_key, item['version'])
        return item


class WandoujiaAppPipeline(object):
    def process_item(self, item, spider):
        wandoujia_collection = spider.collection
        row = wandoujia_collection.find_one({'package_name': item['package_name'], 'vname': item['vname']})
        if not row:
            wandoujia_collection.insert_one({
                'app_name': item['app_name'],
                'package_name': item['package_name'],
                'app_id': item['app_id'],
                'app_vid': item['app_vid'],
                'vcode': item['vcode'],
                'vname': item['vname'],
                'icon': item['icon'],
                'category_id': item['category_id'],
                'install': item['install'],
                'praise': item['praise'],
                'comment_count': item['comment_count'],
                'category': item['category'],
                'tag': item['tag'],
                'app_update_dt': item['app_update_dt'],
                'system': item['system'],
                'permission': item['permission'],
                'company': item['company'],
                'desc': item['desc'],
                'change': item['change'],
                'update_dt': datetime.datetime.now()
            })
            print 'http://www.wandoujia.com/apps/%s %s' % (item['package_name'], item['app_name'])