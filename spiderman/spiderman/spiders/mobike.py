#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import datetime
import json

import scrapy

from spiderman import items
from spiderman.model.base import PG_DB as db
from spiderman.model import mobike


class Mobike(scrapy.Spider):
    name = 'mobike'
    db = db
    models = {
        'bike': mobike.spider_mobike_bike,
        'status': mobike.spider_mobike_status
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'spiderman.pipelines.MobikePipeline': 999,
        }
    }

    def start_requests(self):
        url = 'https://apiv2.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
        form_data = {
            'longitude': '116.331551',
            'latitude': '40.002086',
            'scope': '100'
        }
        yield scrapy.http.FormRequest(url=url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        item = items.MobikeItem()
        now = str(datetime.datetime.now())
        if response.body_as_unicode():
            r = json.loads(response.body_as_unicode())
            for i in r.get('object'):
                item['bike_id'] = i.get('bikeIds')
                item['longitude'] = i.get('distX')
                item['latitude'] = i.get('distY')
                item['bike_type'] = i.get('biketype')
                item['datetime'] = now
                print item['bike_id']
                # yield item
        else:
            self.logger.warning('No Response', response.url)
