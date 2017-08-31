#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

import os
import random
from peewee import *

PG_DB = PostgresqlDatabase('mydb', user='tk', password='tk0306', host='localhost')

class BasePipeline(object):
    def open_spider(self, spider):
        spider.db.connect()
        for model in spider.models.values():
            spider.db.create_table(model, safe=True)

    def close_spider(self, spider):
        spider.db.close()


class CommonRequestMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        # print 'this is common request'
        user_agent_list = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'user_agent.cfg')).read().split('\n')
        ua = random.choice(user_agent_list)
        if ua:
            request.headers['User-Agent'] = ua
        request.headers['Accept'] = '*/*'
        request.headers['Accept-Encoding'] = 'gzip, deflate, sdch'
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
        request.headers['Connection'] = 'keep-alive'
        return


class ProxyMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        # print 'this is proxy middleware'
        proxy_url = 'http://pi.tiankun.me:1081'
        request.meta['proxy'] = proxy_url
        return

