#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30


from peewee import *
from base import PG_DB as db

class spider_siwei_speed(Model):
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
