#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import DEFAULT_DB as db
import datetime


class spide_app_baidu(Model):
    app_id = CharField()
    type = CharField()
    subtype = CharField()
    name = CharField()
    score = CharField(null=True)
    tag = CharField(null=True)
    size = CharField(null=True)
    version = CharField(null=True)
    download_num = CharField(null=True)
    description = TextField(null=True)
    package = CharField(null=True)
    download_link = TextField(null=True)
    create_time = DateTimeField()

    class Meta:
        database = db
        schema = 'app'


if '__main__' == __name__:
    row = spide_app_baidu.select().where(spide_app_baidu.app_id=='22113516').get()
    row.score = '79'
    row.save()