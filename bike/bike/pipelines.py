# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from base import BasePipeline

# class BasePipeline(object):
#     def open_spider(self, spider):
#         spider.db.connect()
#         for model_tmp in spider.models.values():
#             spider.db.create_table(model_tmp, safe=True)
#
#     def close_spider(self, spider):
#         spider.db.close()


class ProxyPipeline(BasePipeline):
    def process_item(self, item, spider):
        check_query = spider.models['proxy'].select().where(
            (spider.models['proxy'].host == item['host'])
            & (spider.models['proxy'].port == item['port'])
            & (spider.models['proxy'].type == item['type'])
        )
        if not check_query.exists():
            spider.models['proxy'].create(
                host=item['host'],
                port=item['port'],
                type=item['type'],
            )
        return item


class MobikePipeline(BasePipeline):
    def insert_item(self, item, spider):
        spider.models['status'].create(
            bike_id=item['bike_id'],
            longitude=item['longitude'],
            latitude=item['latitude'],
            appear_time=item['datetime'],
            last_time=item['datetime'],
        )

    def update_finish_status(self, item, spider):
        spider.models['status'].update(finish=True).where(
            (spider.models['status'].bike_id == item['bike_id'])
            & (spider.models['status'].finish == False)
        ).execute()

    def update_last_time(self, item, spider):
        spider.models['status'].update(last_time=item['datetime']).where(
            (spider.models['status'].bike_id == item['bike_id'])
            & (spider.models['status'].longitude == item['longitude'])
            & (spider.models['status'].latitude == item['latitude'])
            & (spider.models['status'].finish == False)
        ).execute()

    def process_item(self, item, spider):
        spider.models['bike'].get_or_create(bike_id=item['bike_id'], bike_type=item['bike_type'])
        check_bike_id_query = spider.models['status'].select().where((spider.models['status'].bike_id == item['bike_id']))
        if not check_bike_id_query.exists():
            self.insert_item(item, spider)
        else:
            check_location_query = check_bike_id_query.where(
                (spider.models['status'].longitude == item['longitude'])
                & (spider.models['status'].latitude == item['latitude'])
            )
            if not check_location_query.exists():
                self.update_finish_status(item, spider)
                self.insert_item(item, spider)
            else:
                check_finish_status_query = check_location_query.where(
                    spider.models['status'].finish == True
                )
                if check_finish_status_query.exists():
                    self.insert_item(item, spider)
                else:
                    self.update_last_time(item, spider)
        return item
