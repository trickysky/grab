# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from base import BasePipeline, DEFAULT_REDIS as r


class SiweiPipeline(BasePipeline):
    def insert_item(self, item, spider, hash_code):
        spider.models['speed'].create(
            hash_code=hash_code,
            time=item['time'],
            speed=item['speed'],
            b_index=item['b_index'],
            c_index=item['c_index'],
            s_index=item['s_index'],
        )

    def process_item(self, item, spider):
        hash_code = hash(
            item['code'] + item['city'] + item['road_name'] + item['start_name'] + item['end_name'] + item['dir'] +
            str(item['kind']))
        if r.exists(hash_code):
            if not r.get(hash_code) == str(item['time']):
                self.insert_item(item, spider, hash_code)
                r.set(hash_code, item['time'])
        else:
            spider.models['road_name'].get_or_create(
                hash_code=hash_code,
                code=item['code'],
                city=item['city'],
                road_name=item['road_name'],
                start_name=item['start_name'],
                end_name=item['end_name'],
                dir=item['dir'],
                kind=item['kind']
            )
            check_query = spider.models['speed'].select().where(
                (spider.models['speed'].hash_code == hash_code) & (spider.models['speed'].time == item['time']))
            if not check_query.exists():
                self.insert_item(item, spider, hash_code)
            r.set(hash_code, item['time'])
        return item


class SiweiRoadPipeline(BasePipeline):
    def process_item(self, item, spider):
        hash_code = hash(
            item['code'] + item['city'] + item['road_name'] + item['start_name'] + item['end_name'] + item['dir'] +
            str(item['kind']))
        spider.models['road_name'].update(geom_str=item['geom_str']).where(
            spider.models['road_name'].hash_code == hash_code).execute()
        return item
