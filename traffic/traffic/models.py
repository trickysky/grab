#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import DEFAULT_DB as db


class spider_traffic_siwei_speed(Model):
    code = CharField(index=True)
    time = DateTimeField(index=True)
    speed = FloatField()
    b_index = FloatField()
    c_index = FloatField()
    s_index = FloatField()
    kind = SmallIntegerField()
    rtic_lon_lats = CharField(null=True)
    vkt = CharField(null=True)

    class Meta:
        database = db


class spider_traffic_siwei_road_name(Model):
    code = CharField(primary_key=True)
    city = CharField()
    road_name = CharField()
    start_name = CharField()
    end_name = CharField()
    dir = CharField()

    class Meta:
        database = db


if '__main__' == __name__:
    spider_traffic_siwei_speed.create()
