#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

import scrapy
import json
from spiderman.model.base import PG_DB as db


class Siwei(scrapy.Spider):
    name = 'siwei'
    db = db
    models = {}
    custom_settings = {}

    def start_requests(self):
        city_list = {
            u'北京': '110000',
            # u'天津': '120000',
            # u'石家庄': '130100',
            # u'太原': '140100',
            # u'沈阳': '210100',
            # u'长春': '220100',
            u'上海': '310000',
            # u'南京': '320100',
            # u'无锡': '320200',
            # u'苏州': '320500',
            # u'杭州': '330100',
            # u'宁波': '330200',
            # u'温州': '330300',
            # u'台州': '331000',
            # u'福州': '350100',
            # u'泉州': '350500',
            # u'厦门': '350200',
            # u'青岛': '370200',
            # u'武汉': '420100',
            # u'长沙': '430100',
            # u'广州': '440100',
            # u'深圳': '440300',
            # u'珠海': '440400',
            # u'东莞': '441900',
            # u'中山': '442000',
            # u'重庆': '500000',
            # u'成都': '510100'
        }
        for city in city_list:
            city_code = city_list[city]
            url = 'http://mobile.trafficeye.com.cn:9000/touChuanWebService/TouchuanService_v2'
            formdata = {
                'cityCode': city_code,
                'method': '10'
            }
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse_detail, meta={'city': city})

    def parse_detail(self, response):
        city = response.meta['city']
        if response.body:
            result = json.loads(response.body)
            print
            # for i in range(len(result)):
                # item = items.siweiItem()
                # item['city'] = city
                # item['time'] = pytz.timezone('Asia/Shanghai').localize(
                #     datetime.datetime.strptime(result[i].get('time'), '%Y%m%d%H%M'))
                # item['name'] = result[i].get('name')
                # item['start'] = result[i].get('startName')
                # item['end'] = result[i].get('endName')
                # item['avg_speed'] = float(result[i].get('avgSpeed')) if result[i].get('avgSpeed') else None
                # item['b_index'] = float(result[i].get('bIndex')) if result[i].get('bIndex') else None
                # item['s_index'] = float(result[i].get('sIndex')) if result[i].get('sIndex') else None
                # item['c_index'] = float(result[i].get('cIndex')) if result[i].get('cIndex') else None
                # item['direction'] = result[i].get('dir')
                # yield item
