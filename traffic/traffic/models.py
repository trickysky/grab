#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import DEFAULT_DB as db


class spider_traffic_siwei_speed(Model):
    city = CharField()
    code = CharField()
    time = DateTimeField()
    speed = FloatField()
    road_name = CharField()
    start_name = CharField()
    end_name = CharField
    dir = CharField()
    b_index = FloatField()
    c_index = FloatField()
    s_index = FloatField()
    kind = SmallIntegerField()
    rtic_lon_lats = CharField(null=True)
    vkt = CharField(null=True)

    class Meta:
        database = db


if '__main__' == __name__:
    spider_traffic_siwei_speed.create(
        # city=item['city'],
        # code=item['code'],
        # time=item['time'],
        # speed=item['speed'],
        # road_name=item['road_name'],
        # start_name=item['start_name'],
        # end_name=item['end_name'],
        # dir=item['dir'],
        # b_index=item['b_index'],
        # c_index=item['c_index'],
        # s_index=item['s_index'],
        # kind=item['kind'],
        # rtic_lon_lats=item['rtic_lon_lats'],
        # vkt=item['vkt']
    )
