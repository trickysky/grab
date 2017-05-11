#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import datetime
import time
import json

import scrapy
from scrapy import log

from spiderman import items


class Mobike(scrapy.Spider):
    name = 'mobike'
    custom_settings = {
        'ITEM_PIPELINES': {
            'spiderman.pipelines.MobikePipeline': 300,
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
                yield item
        else:
            log.msg('No Response', level=log.CRITICAL)
