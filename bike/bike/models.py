#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import PG_DB as db


class spider_mobike_bike(Model):
    bike_id = CharField(primary_key=True)
    bike_type = SmallIntegerField()

    class Meta:
        database = db


class spider_mobike_status(Model):
    bike_id = CharField(index=True)
    longitude = CharField(index=True)
    latitude = CharField(index=True)
    appear_time = DateTimeField()
    last_time = DateTimeField()
    finish = BooleanField(default=False, index=True)

    class Meta:
        database = db


if '__main__' == __name__:
    spider_mobike_bike.update(bike_type=3).where(spider_mobike_bike.bike_id == '0104234692').execute()
