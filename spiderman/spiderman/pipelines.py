# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from model import mobike


class MobikePipeline(object):
    def __init__(self):
        self.db = mobike.db
        self.mobike_bike = mobike.spider_mobike_bike
        self.mobike_status = mobike.spider_mobike_status

    def open_spider(self, spider):
        self.db.connect()
        self.db.create_table(self.mobike_bike, safe=True)
        self.db.create_table(self.mobike_status, safe=True)

    def close_spider(self, spider):
        self.db.close()

    def insert_item(self, item):
        self.mobike_status.create(
            bike_id=item['bike_id'],
            longitude=item['longitude'],
            latitude=item['latitude'],
            appear_time=item['datetime'],
            last_time=item['datetime'],
        )

    def update_finish_status(self, item):
        self.mobike_status.update(finish=True).where(
            (self.mobike_status.bike_id == item['bike_id'])
            & (self.mobike_status.finish == False)
        ).execute()

    def update_last_time(self, item):
        self.mobike_status.update(last_time=item['datetime']).where(
            (self.mobike_status.bike_id == item['bike_id'])
            & (self.mobike_status.longitude == item['longitude'])
            & (self.mobike_status.latitude == item['latitude'])
            & (self.mobike_status.finish == False)
        ).execute()

    def process_item(self, item, spider):
        self.mobike_bike.get_or_create(bike_id=item['bike_id'], bike_type=item['bike_type'])
        check_bike_id_query = self.mobike_status.select().where((self.mobike_status.bike_id == item['bike_id']))
        if not check_bike_id_query.exists():
            self.insert_item(item)
        else:
            check_location_query = check_bike_id_query.where(
                (self.mobike_status.longitude == item['longitude'])
                & (self.mobike_status.latitude == item['latitude'])
            )
            if not check_location_query.exists():
                self.update_finish_status(item)
                self.insert_item(item)
            else:
                check_finish_status_query = check_location_query.where(
                    self.mobike_status.finish == True
                )
                if check_finish_status_query.exists():
                    self.insert_item(item)
                else:
                    self.update_last_time(item)
        return item
