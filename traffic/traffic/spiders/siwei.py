# -*- coding: utf-8 -*-
import scrapy
from traffic import items
from traffic.models import *

import json, pytz, datetime

class SiweiSpider(scrapy.Spider):
    name = 'siwei'
    db = db
    # allowed_domains = ['siwei.co']
    # start_urls = ['http://siwei.co/']
    models = {
        'speed': spider_traffic_siwei_speed
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'traffic.pipelines.SiweiPipeline': 999,
        }
    }


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
            for i in result:
                item = items.SiweiItem()
                item['city'] = city
                item['code'] = i.get('code')
                item['time'] = pytz.timezone('Asia/Shanghai').localize(
                    datetime.datetime.strptime(i.get('time'), '%Y%m%d%H%M'))
                item['speed'] = float(i.get('avgSpeed'))
                item['road_name'] = i.get('name')
                item['start_name'] = i.get('startName')
                item['end_name'] = i.get('endName')
                item['dir'] = i.get('dir')
                item['b_index'] = float(i.get('bIndex'))
                item['c_index'] = float(i.get('cIndex'))
                item['s_index'] = float(i.get('sIndex'))
                item['kind'] = int(i.get('kind'))
                item['rtic_lon_lats'] = i.get('rticLonlats')
                item['vkt'] = i.get('vkt')
                yield item
        else:
            self.logger.warning('No Response', response.url)
