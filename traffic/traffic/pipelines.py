# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from base import BasePipeline


class SiweiPipeline(BasePipeline):
    def insert_item(self, item, spider):
        spider.models['speed'].create(
            code=item['code'],
            time=item['time'],
            speed=item['speed'],
            b_index=item['b_index'],
            c_index=item['c_index'],
            s_index=item['s_index'],
            kind=item['kind'],
            rtic_lon_lats=item['rtic_lon_lats'],
            vkt=item['vkt']
        )

    def process_item(self, item, spider):
        spider.models['road_name'].get_or_create(
            code=item['code'],
            city=item['city'],
            road_name=item['road_name'],
            start_name=item['start_name'],
            end_name=item['end_name'],
            dir=item['dir']
        )
        check_query = spider.models['speed'].select().where(
            (spider.models['speed'].code == item['code']) & (spider.models['speed'].time == item['time']))
        if not check_query.exists():
            self.insert_item(item,spider)
        else:
            pass
        return item
