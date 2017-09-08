#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import DEFAULT_DB as db


class spider_traffic_siwei_speed(Model):
    hash_code = CharField(index=True)
    time = DateTimeField(index=True)
    speed = FloatField()
    b_index = FloatField()
    c_index = FloatField()
    s_index = FloatField()

    class Meta:
        database = db
        schema = 'traffic'


class spider_traffic_siwei_road_name(Model):
    hash_code = CharField(primary_key=True)
    code = CharField()
    city = CharField()
    road_name = CharField()
    start_name = CharField()
    end_name = CharField()
    dir = CharField()
    kind = SmallIntegerField()
    geom_str = TextField(null=True)

    class Meta:
        database = db
        schema = 'traffic'


if '__main__' == __name__:
    a = spider_traffic_siwei_road_name.select()
    for i in a:
        print a.road_name
